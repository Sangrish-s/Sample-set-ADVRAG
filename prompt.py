ENHANCE_QUERY_PROMPT = """Enhance the following user query for a more effective database search. 
The enhanced query should:
1. Expand on key concepts
2. Include relevant synonyms
3. Be more specific and detailed
4. Be formatted as a clear, concise search query

Original query: {user_input}

Enhanced query:"""

SELECT_DOCUMENT_PROMPT = """Task: Select the most relevant document to answer the given query.

Instructions:
1. You MUST choose one document from the list provided below.
2. Do NOT suggest any document not in this list.
3. If none seem particularly relevant, choose the least irrelevant one.
4. Respond ONLY with the exact name of the chosen document.
5. Do NOT add any explanation or additional text.

Available documents:
{document_names}

Query: {query}

Document Summaries:
{summaries_text}

Selected document name:"""

ANSWER_PROMPT = """Based on the following context and the original query, please provide a comprehensive answer. 
If the answer is not fully contained in the context, say so and provide the best possible answer based on the available information.

Original query: {user_input}
Enhanced query used for search: {enhanced_query}

Context: {context}

Answer:"""

SUMMARIZE_DOCUMENT_PROMPT = """Summarize the following text in 2-3 sentences:

{first_500_words}"""