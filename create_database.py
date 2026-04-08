from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

data = PyPDFLoader("document_Loaders/deeplearning.pdf")
docs = data.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200 )
chunks = splitter.split_documents(docs)
embedding_model = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma.from_documents( 
    documents=chunks, 
    embedding=embedding_model, 
    persist_directory="./chroma_db")
