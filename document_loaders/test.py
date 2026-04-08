from langchain_community.document_loaders import TextLoader 
from langchain_text_splitters import CharacterTextSplitter

data = TextLoader("document_loaders/notes.txt")
docs = data.load()

splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 1, separator = "\n")
chunks = splitter.split_documents(docs) 

print(len(chunks))
print(chunks[0].page_content) 
