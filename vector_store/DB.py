from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document 


embedding = HuggingFaceEmbeddings(
model = "sentence-transformers/all-MiniLM-L6-v2"
)

docs = [
    Document(page_content="Python is widely used in AI and machine learning.", metadata={"source": "doc1"}),
    Document(page_content="Pandas is used for data analysis and manipulation.", metadata={"source": "doc2"}),
    Document(page_content="Numpy is a library for numerical computations in Python.", metadata={"source": "doc3"})
]

embedding_model = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma.from_documents(documents=docs, embedding=embedding_model, persist_directory="./chroma_db")
 
result = vector_store.similarity_search("what is used for data analysis?",k=2)

for r in result:
    print(r.page_content)
    print(r.metadata)

retriver = vector_store.as_retriever()

docs = retriver.invoke("Explain the use of Numpy in Python?")

for d in docs:
    print(d.page_content)