import asyncio
from mistralai import Mistral
from langchain.text_splitter import TokenTextSplitter
import chromadb
from chromadb.config import Settings
import PyPDF2
from tenacity import retry, stop_after_attempt, wait_exponential
from prompt import ENHANCE_QUERY_PROMPT, SELECT_DOCUMENT_PROMPT, ANSWER_PROMPT, SUMMARIZE_DOCUMENT_PROMPT

class EnhancedRAG:
    def __init__(self, api_key, model):
        self.mistral_client = Mistral(api_key=api_key)
        self.model = model
        self.chroma_client = chromadb.Client(Settings(persist_directory="./chroma_db"))
        self.text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=100)
        self.collections = {}
        self.summaries = {}

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def generate_mistral_response(self, prompt: str) -> str:
        def api_call():
            try:
                response = self.mistral_client.chat.complete(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}]
                )
                if response and response.choices and response.choices[0].message.content:
                    return response.choices[0].message.content
            except Exception as e:
                print(f"Error in Mistral API call: {str(e)}")
            return ""

        try:
            result = await asyncio.to_thread(api_call)
            return result
        except Exception as e:
            print(f"Unexpected error in generate_mistral_response: {str(e)}")
            return ""

    async def read_pdf(self, file) -> str:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    async def summarize_document(self, doc_text: str, doc_name: str) -> str:
        first_500_words = ' '.join(doc_text.split()[:500])
        prompt = SUMMARIZE_DOCUMENT_PROMPT.format(first_500_words=first_500_words)
        summary = await self.generate_mistral_response(prompt)
        self.summaries[doc_name] = summary
        return summary

    async def process_and_add_document(self, document: str, doc_name: str):
        collection_name = f"collection_{doc_name.replace('.pdf', '')}"
        collection = self.chroma_client.get_or_create_collection(collection_name)
        self.collections[doc_name] = collection

        chunks = self.text_splitter.split_text(document)
        for i, chunk in enumerate(chunks):
            collection.add(
                documents=[chunk],
                metadatas=[{"chunk_id": i}],
                ids=[f"chunk_{i}"]
            )

        await self.summarize_document(document, doc_name)

    async def enhance_query(self, user_input: str) -> str:
        prompt = ENHANCE_QUERY_PROMPT.format(user_input=user_input)
        enhanced_query = await self.generate_mistral_response(prompt)
        return enhanced_query

    async def select_document(self, query: str) -> str:
        if not self.summaries:
            return "No documents available"

        summaries_text = "\n\n".join([f"{name}: {summary}" for name, summary in self.summaries.items()])
        document_names = list(self.summaries.keys())
        
        prompt = SELECT_DOCUMENT_PROMPT.format(
            document_names=', '.join(document_names),
            query=query,
            summaries_text=summaries_text
        )

        selected_doc = await self.generate_mistral_response(prompt)
        selected_doc = selected_doc.strip().strip('"')  # Remove any extra whitespace and quotes
        
        # If the selected document is not in our list, default to the first document
        if selected_doc not in document_names:
            selected_doc = document_names[0]
        
        return selected_doc

    async def query(self, user_input: str, doc_name: str = None) -> dict:
        enhanced_query = await self.enhance_query(user_input)
        
        if not doc_name:
            doc_name = await self.select_document(enhanced_query)

        collection = self.collections.get(doc_name)
        if not collection:
            return {
                "error": f"No document named '{doc_name}' found.",
                "selected_document": doc_name,
                "enhanced_query": enhanced_query
            }

        results = collection.query(query_texts=[enhanced_query], n_results=3)
        context = ""
        for doc, metadata in zip(results['documents'][0], results['metadatas'][0]):
            context += f"From {doc_name}, Chunk {metadata['chunk_id']}:\n{doc}\n\n"
        
        answer_prompt = ANSWER_PROMPT.format(
            user_input=user_input,
            enhanced_query=enhanced_query,
            context=context
        )
        
        answer = await self.generate_mistral_response(answer_prompt)
        
        return {
            "answer": answer,
            "enhanced_query": enhanced_query,
            "selected_document": doc_name
        }

    async def upload_documents(self, uploaded_files):
        for uploaded_file in uploaded_files:
            doc_name = uploaded_file.name
            doc_text = await self.read_pdf(uploaded_file)
            await self.process_and_add_document(doc_text, doc_name)