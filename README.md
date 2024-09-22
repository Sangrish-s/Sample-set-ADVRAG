# Enhanced RAG System

This project implements an Enhanced Retrieval-Augmented Generation (RAG) system using Streamlit, Mistral AI, and ChromaDB.

## Mistral API key: wOKx3udNkGUEtjzY8wxWQ4OrovxguCej

#### Please use as necessary, this is also the password on the left of the image

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
   MISTRAL_API_KEY= wOKx3udNkGUEtjzY8wxWQ4OrovxguCej
   ```

## Usage

1. Run the Docker container:
   ```
   docker run -p 8088:8088 -v $(pwd):/app --env-file .env enhanced-rag
   ```

2. Open a web browser and go to `http://localhost:8088`

3. Use the Streamlit interface to:
   - Upload PDF documents
   - Process documents (Depends on size for 2MB worth of document or more than 250 pages it takes around a Minute)
   - Query the RAG system

4. Please checkout this youtube video for ideal usecase
   - Link: 

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
