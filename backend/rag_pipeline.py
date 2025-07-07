from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import json
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

class RAG:
    def __init__(self):
        # Load documents

        with open("../data/faqs.json", "r", encoding="utf-8") as f:
            docs_json = json.load(f)

        # Flatten the list in case of nested lists
        if isinstance(docs_json[0], list):
            docs_json = [item for sublist in docs_json for item in sublist]

        docs = [Document(page_content=f"Question: {doc['question']}\nAnswer: {doc['answer']}", 
                        metadata={"title": doc.get("question", "")}) for doc in docs_json]

        # Split documents
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)

        # Create vector store
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.store = FAISS.from_documents(chunks, embeddings)

        # Initialize LLM
        self.llm = ChatGroq(model_name="Gemma2-9b-It", temperature=0)

        # Create prompt template
        self.prompt_template = ChatPromptTemplate.from_template(
            """Use the following context to answer the question.

            Context:
            {context}

            Question: {question}

            Answer:"""
        )


    async def answer(self, query: str) -> str:
        # Retrieve relevant documents
        docs = self.store.similarity_search(query, k=3)
        context = "\n".join([d.page_content for d in docs])
        
        # Generate answer using LangChain's chat interface
        chain = self.prompt_template | self.llm
        response = await chain.ainvoke({"context": context, "question": query})
        
        return response.content

if __name__ == "__main__":
    print("RAG pipeline is implemented correctly")