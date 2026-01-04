# lamma index to load the pdf document and embed them
from llama_index.readers.file import PDFReader,EpubReader,MarkdownReader
from llama_index.core.node_parser import SentenceSplitter
import ollama

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=250) # represents characters not words

def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [d.text for d in docs if getattr(d, "text", None)]
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks

def embed_text(texts: list[str]) -> list[list[float]]:
    response = ollama.embed(
        model='bge-m3:567m',
        input=texts
    )
    return response['embeddings']