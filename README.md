# Enhanced RAG System

This project implements an Enhanced Retrieval-Augmented Generation (RAG) system using Streamlit, Mistral AI, and ChromaDB.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Sangrish-s/enhanced-rag.git
   cd enhanced-rag
   ```

2. Install Docker if you haven't already. [Docker Installation Guide](https://docs.docker.com/get-docker/)

3. Build the Docker image:
   ```
   docker build -t enhanced-rag .
   ```

4. Create a `.env` file in the project root and add your Mistral API key:
   ```
   MISTRAL_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Docker container:
   ```
   docker run -p 8088:8088 -v $(pwd):/app --env-file .env enhanced-rag
   ```

2. Open a web browser and go to `http://localhost:8088`

3. Use the Streamlit interface to:
   - Upload PDF documents
   - Process documents
   - Query the RAG system

## Features

- Document upload and processing
- Automatic document summarization
- Enhanced query processing
- Multi-document querying
- Interactive web interface

## Troubleshooting

If you encounter any issues:
1. Ensure Docker is running and you have necessary permissions.
2. Check that your Mistral API key is correctly set in the `.env` file.
3. Verify that all required files are present in the project directory.

For more detailed information, refer to the documentation README.
