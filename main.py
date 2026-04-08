from dotenv import load_dotenv 
from langchain_mistralai import ChatMistralAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate 
from langchain_community.vectorstores import Chroma
# from langchain_text_splitters import RecursiveCharacterTextSplitter 
# from langchain_community.document_loaders import TextLoader, PyPDFLoader

load_dotenv()

# data = TextLoader("document_Loaders/notes.txt")
# data = PyPDFLoader("document_Loaders/GRU.pdf")
# data = PyPDFLoader("document_Loaders/deeplearning.pdf")
# docs = data.load()

# splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200 )
# chunks = splitter.split_documents(docs)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = vector_store.as_retriever(
    search_type = "mmr",
    search_kwargs = {
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5 
    } 
)

llm = ChatMistralAI(model="mistral-small-2506")

# template = ChatPromptTemplate.from_messages([
#     ("system", "You are an AI that summarizes the document."),
#     ("human", "{data}")
# ])

# prompt = template.format_messages(data=chunks[0].page_content)
# response = model.invoke(prompt)
# print(response.content)

#prompt template 
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
        ),
        (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
    ]
)

print("Rag system created ")

print("press 0 to exit ")

while True:
    query = input("You : ")
    if query == "0":
        break 
    
    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    
    final_prompt = prompt.invoke({
        "context" :context,
        "question": query
    })
    
    response = llm.invoke(final_prompt)

    print(f"\n AI: {response.content}")
    
