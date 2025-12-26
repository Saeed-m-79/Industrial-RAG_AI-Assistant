from langchain_community.vectorstores.faiss import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter




#HERE WE READ THE RAW TEXT
def load_manual_text(path : str) -> str :
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
    

#CHUNK
def chunk_text(text : str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 400,
        chunk_overlap = 50
                )
    return splitter.split_text(text)


#EMBEDDING THE CHUNKS
def build_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_texts(chunks, embedding = embeddings)
    return vectorstore

#READY :)

#RETRIVAL(didn't write the code on my own - GPTed!!!)

#RETRIEVAL
def retrieve_context(vectorstore, query: str, k: int = 3) -> str:
    docs = vectorstore.similarity_search(query, k=k)
    return "\n\n".join(doc.page_content for doc in docs)



