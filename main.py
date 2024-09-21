import streamlit as st
import asyncio
from utils import EnhancedRAG

# Streamlit page config
st.set_page_config(page_title="Enhanced RAG System", layout="wide")

# Custom CSS for a cooler look
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #4CAF50;
        border-radius: 5px;
    }
    .stTextInput>div>div>input {
        color: #ffffff;
        background-color: #262730;
    }
    .stSelectbox>div>div>select {
        color: #ffffff;
        background-color: #262730;
    }
    .result-box {
        background-color: #1e1e2e;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
    .summary-box {
        background-color: #2a2a3a;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for API key input
st.sidebar.title("Configuration")
API_KEY = st.sidebar.text_input("Enter Mistral API Key:", type="password")
MODEL = "mistral-small-latest"

# Initialize session state
if 'rag' not in st.session_state:
    st.session_state.rag = None
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []

# Main app
st.title("🚀 Enhanced RAG System")

# File uploader
uploaded_files = st.file_uploader("Choose PDF files", accept_multiple_files=True, type="pdf")

if uploaded_files:
    if st.button("Process Documents"):
        st.session_state.rag = EnhancedRAG(API_KEY, MODEL)
        with st.spinner("Processing documents..."):
            asyncio.run(st.session_state.rag.upload_documents(uploaded_files))
        st.session_state.uploaded_files = [file.name for file in uploaded_files]
        st.success("Documents processed successfully!")

# Display document summaries
if st.session_state.rag:
    st.subheader("📚 Query Your Documents")
    
    query = st.text_input("Enter your query:")
    
    if st.button("🔍 Search"):
        if query:
            with st.spinner("Searching..."):
                try:
                    result = asyncio.run(st.session_state.rag.query(query))
                    st.subheader("🔮 Result")
                    st.markdown(f'<div class="result-box">', unsafe_allow_html=True)
                    
                    if isinstance(result, dict):
                        if 'selected_document' in result:
                            st.markdown(f"**Selected Document:** {result['selected_document']}")
                        if 'enhanced_query' in result:
                            st.markdown(f"**Enhanced Query:** {result['enhanced_query']}")
                        if 'answer' in result:
                            st.markdown("**Answer:**")
                            st.write(result['answer'])
                        else:
                            st.write(result)  # Fallback if 'answer' is not present
                    else:
                        st.write(result)  # Display the result as is if it's not a dictionary
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"An error occurred while processing your query: {str(e)}")
        else:
            st.warning("Please enter a query.")
else:
    st.info("Please upload and process documents to start querying.")

# Footer
st.markdown("---")
st.markdown("Built for SampleSet")