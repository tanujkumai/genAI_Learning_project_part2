from langchain_community.document_loaders import WebBaseLoader

url = ["https://www.apple.com/in/macbook-pro/","https://www.myntra.com/mac"]

data = WebBaseLoader(url)
docs = data.load()

print(len(docs))