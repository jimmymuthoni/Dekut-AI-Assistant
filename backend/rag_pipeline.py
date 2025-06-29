from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline
import json
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['HUGGING_FACE_TOKEN'] = os.getenv("HUGGING_FACE_TOKEN")

class RAG:
    def __init__(self):
        with open("../data/docs.json", "r", encoding="utf-8") as f:
            docs_json = json.load(f)
        docs = [Document(page_content=doc["text"], metadata={"title": doc.get("title", "")}) for doc in docs_json]
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)
        embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.store = FAISS.from_documents(chunks, embedding)
        self.llm = pipeline("text-generation", model="google/flan-t5-base", tokenizer="google/flan-t5-base")

    async def answer(self, query: str) -> str:
        docs = self.store.similarity_search(query, k=3)
        context = "\n".join([d.page_content for d in docs])
        prompt = f"Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
        response = self.llm(prompt, max_length=512, temperature=0)
        answer = response[0]['generated_text'].split("Answer:")[-1].strip()

        return answer
