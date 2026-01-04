# 🚀 Qwen3 RAG Pipeline

**Production-ready RAG system** with local inference, durable workflows, and full observability.

[
[

## ✨ Features
- **Qwen3:1.7B** - Lightweight, multilingual LLM via Ollama
- **GE-M3:567M** - Open-source embeddings (384-dim)
- **Qdrant** - Vector database with hybrid search
- **Inngest** - Durable workflows with step-level retries
- **FastAPI** - Production API with Swagger docs
- **Streamlit** - Interactive chat UI
- **LlamaIndex** - Advanced document chunking

## 🏗️ Architecture
```
PDF → LlamaIndex (chunk) → GE-M3 Embed → Qdrant → Inngest RAG → Qwen3 → Answer
                           (FastAPI + Streamlit UI)
```

## 🚀 Quick Start

1. **Clone & Install**
```bash
git clone https://github.com/SHREE/rag-project.git
cd rag-project
conda create -n rag python=3.10
conda activate rag
pip install -r requirements.txt
```

2. **Start Services**
```bash
# Terminal 1: Ollama
ollama serve &
ollama pull qwen3:1.7b
ollama pull ge-m3:567m  # Embeddings

# Terminal 2: Qdrant
docker run -p 6333:6333 qdrant/qdrant

# Terminal 3: API
uvicorn main:app --reload
```

3. **Frontend**
```bash
streamlit run streamlit_app.py
```

## 📝 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/ingest` | Upload PDF for indexing |
| `POST` | `/query` | RAG query with sources |
| `GET` | `/docs` | Interactive Swagger UI |

**Test Query:**
```bash
curl -X POST "http://localhost:8000/ingest" \
  -H "Content-Type: application/json" \
  -d '{"pdf_path": "sample.pdf"}'

curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is RAG?", "top_k": 5}'
```

## 🛠️ Project Structure
```
rag-project/
├── main.py           # FastAPI + Inngest workflows
├── vector_db.py      # Qdrant storage
├── data_loader.py    # LlamaIndex chunking
├── streamlit_app.py  # Chat UI
├── requirements.txt
├── .env.example      # Copy to .env
└── README.md
```

## 🔧 Configuration
Copy `.env.example` → `.env`:
```env
OLLAMA_BASE_URL=http://host.docker.internal:11434
QDRANT_URL=http://localhost:6333
EMBEDDING_DIM=384
```

## 📈 Monitoring
- **Inngest Dashboard**: Workflow traces, retries, metrics
- **FastAPI /metrics**: Prometheus endpoint
- **Ollama Logs**: `ollama ps`

## 🔍 Troubleshooting
| Issue | Solution |
|-------|----------|
| Qdrant connection | `docker run -p 6333:6333 qdrant/qdrant` |
| Ollama 404 | `ollama serve & ollama pull qwen3:1.7b` |
| Embedding dim mismatch | Check `EMBEDDING_DIM=384` in `.env` |

## 🎯 Why This Stack?
- **Local-first**: Zero API costs, full privacy
- **Durable**: Inngest retries failed embeddings/RAG steps
- **Scalable**: FastAPI async + Qdrant clustering-ready
- **Modern**: TypeScript-level DX with Pydantic + Inngest types

## 📄 License
MIT License - Use freely in commercial projects! [LICENSE](LICENSE)

## 🙌 Contributing
1. Fork & PR
2. Update tests: `pytest`
3. Follow PEP8: `black .`

**⭐ Star if useful!** Questions? [Open issue](https://github.com/SHREE/rag-project/issues)
