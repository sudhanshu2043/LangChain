from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='D:\GenAi\LangChain\9.DocumentLoader\Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])