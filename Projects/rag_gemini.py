import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

os.environ["GOOGLE_API_KEY"] = "masukkan api key"

loader = TextLoader("data_pribadi.txt")
dokumen = loader.load()

text_splitter = CharacterTextSplitter(chunk_size= 50, chunk_overlap=10)
chunks = text_splitter.split_documents(dokumen)