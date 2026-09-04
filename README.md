# 📚 Multi-PDF RAG Chatbot using LangChain

## Overview

This project is a Retrieval-Augmented Generation (RAG) application that allows users to ask questions across multiple PDF documents.

Instead of relying solely on the language model's knowledge, the chatbot retrieves relevant information from uploaded PDFs and generates context-aware answers.

---

## Features

✅ Multi-PDF Support

✅ Semantic Search using FAISS

✅ HuggingFace Embeddings (BAAI/bge-small-en-v1.5)

✅ OpenRouter LLM Integration

✅ Context-Aware Responses

✅ Source Document Tracking

✅ Fast Retrieval Pipeline

---

## Tech Stack

* Python
* LangChain
* FAISS Vector Database
* HuggingFace Embeddings
* OpenRouter
* PyPDF
* Retrieval-Augmented Generation (RAG)

---

## Architecture

PDF Files

↓

Document Loading (PyPDFLoader)

↓

Text Chunking (RecursiveCharacterTextSplitter)

↓

Embeddings (BAAI/bge-small-en-v1.5)

↓

FAISS Vector Store

↓

Retriever

↓

OpenRouter LLM

↓

Final Answer

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/multi-pdf-rag-chatbot-langchain.git
cd multi-pdf-rag-chatbot-langchain
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## Run Project

```bash
python app.py
```

---

## Example

Question:

```text
What are the main topics covered in the documents?
```

Answer:

```text
The documents discuss...
```

---

## Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Prompt Engineering
* LangChain Framework
* LLM Integration
* Information Retrieval
* Embedding Models
* Production-Ready AI Pipelines

---

## Future Improvements

* Streamlit Web Interface
* PDF Upload Support
* Conversation Memory
* Source Citation Display
* Hybrid Search (Keyword + Semantic)

---

## Author

Sandeep Pilli

Diploma AI & ML Student | GenAI Enthusiast | Building AI Projects with LangChain, RAG, and LLMs.
