# 🧠 WellNet — Medical AI Chatbot using Llama-2

A powerful **medical AI chatbot** built using the **Llama-2-7B-Chat-GGML language model** and medical knowledge from *The Gale Encyclopedia of Medicine*.  
This system combines **Large Language Models (LLMs)** with **vector search, embeddings, and retrieval-augmented generation (RAG)** to answer medical questions accurately.

⚠️ **Disclaimer:** This tool is for informational purposes only and is **NOT** a substitute for professional medical advice.

---

## 🔍 Project Overview

WellNet is an **AI-powered medical assistant** designed to:
- Understand natural language
- Search a trusted medical knowledge base
- Generate accurate, contextual responses

The system uses:
- **LLaMA-2** for reasoning and text generation  
- **Sentence Transformers** for embeddings  
- **LangChain** for LLM orchestration  
- **Vector databases (Pinecone / FAISS)** for fast similarity search  
- **Flask + Bootstrap** for a clean web interface  

The chatbot runs fully on **CPU** — no GPU required — making it accessible on normal laptops.

---

## 🧠 Key Features

✔ Natural language medical Q&A  
✔ Knowledge-based answers from real medical references  
✔ Context-aware conversations  
✔ Retrieval-Augmented Generation (RAG)  
✔ Vector similarity search  
✔ CPU-only execution  
✔ Web-based UI  
✔ Modular, reusable, scalable codebase  

---

## 🧰 Tech Stack

| Technology | Purpose |
|----------|---------|
| Python | Core backend |
| Llama-2-7B-Chat-GGML | Large Language Model |
| LangChain | LLM orchestration |
| Sentence Transformers | Text embeddings |
| Pinecone / FAISS | Vector search |
| Flask | Backend web server |
| Bootstrap | UI styling |
| PDF Loader | Medical document processing |

---

## 📦 Repository Structure

wellnet-using-llama/
│
├── model/ # LLaMA-2 model loading & inference
├── data/ # Medical PDFs (Gale Encyclopedia)
├── embeddings/ # Generated vector embeddings
├── vector_store/ # Pinecone / FAISS indexes
│
├── src/
│ ├── loader.py # Load PDFs
│ ├── chunker.py # Split text into chunks
│ ├── embedder.py # Generate embeddings
│ ├── retriever.py # Fetch relevant medical content
│ ├── chatbot.py # LLM + RAG pipeline
│ └── config.py # Environment & model config
│
├── templates/ # Flask HTML templates
├── static/ # CSS, JS, images
│
├── app.py # Flask app entry
├── store_index.py # Build vector database
├── requirements.txt
└── README.md
