# Enhanced RAG System Documentation

# Mistral API : wOKx3udNkGUEtjzY8wxWQ4OrovxguCej

# Please use this for all purposes

## System Overview

The Enhanced RAG (Retrieval-Augmented Generation) system is designed to provide intelligent responses to queries by leveraging a knowledge base of uploaded documents. It combines the power of Mistral AI for language processing, ChromaDB for efficient vector storage and retrieval, and Streamlit for a user-friendly interface.

## Components

1. **Streamlit Interface** (`main.py`):
   - Handles user interactions
   - Manages document uploads
   - Displays query results

2. **RAG Core** (`utils.py`):
   - Implements the `EnhancedRAG` class
   - Manages document processing and storage
   - Handles query processing and response generation

3. **Prompt Templates** (`prompt.py`):
   - Contains templates for various AI prompts used in the system

4. **Docker Configuration** (`Dockerfile`):
   - Ensures consistent deployment across different environments

## Key Features

1. **Document Processing**:
   - Uploads and processes PDF documents
   - Automatically generates summaries for uploaded documents
   - Stores document content and embeddings in ChromaDB

2. **Query Enhancement**:
   - Improves user queries for more effective information retrieval
   - Selects the most relevant document(s) for a given query

3. **Multi-Document Querying**:
   - Retrieves information from multiple documents when necessary
   - Synthesizes information to provide comprehensive answers

4. **Mistral AI Integration**:
   - Leverages Mistral AI for advanced language understanding and generation
   - Customizable prompts for various tasks (summarization, query enhancement, etc.)

5. **Efficient Information Retrieval**:
   - Uses ChromaDB for fast and efficient vector-based information retrieval

## Workflow

1. User uploads documents through the Streamlit interface
2. System processes documents, generates summaries, and stores information in ChromaDB
3. User submits a query
4. System enhances the query and selects relevant document(s)
5. System retrieves relevant information from ChromaDB
6. Mistral AI generates a response based on the retrieved information
7. Response is displayed to the user through the Streamlit interface

## Configuration

- Mistral API key: Set in the `.env` file
- ChromaDB settings: Configured in `utils.py`
- Streamlit settings: Customizable in `main.py`

## Extending the System

To add new features or modify existing ones:
1. Update the relevant Python files (`main.py`, `utils.py`, or `prompt.py`)
2. Modify the Dockerfile if new dependencies are added
3. Update the `requirements.txt` file with any new Python package requirements
4. Rebuild the Docker image

## Troubleshooting

Common issues and their solutions:
- API key errors: Verify the Mistral API key in the `.env` file
- Docker-related issues: Ensure Docker is installed and running correctly
- Document processing errors: Check supported file formats and file integrity

For further assistance, consult the project maintainers or refer to the individual component documentations (Streamlit, Mistral AI, ChromaDB).
