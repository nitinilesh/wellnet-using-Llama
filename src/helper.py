from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

#Extract data from the FILE
def file(database):
    loader = DirectoryLoader(database,
                    glob="*.pdf",
                    loader_cls=PyPDFLoader)
    
    text_documents = loader.load()

    return text_documents

#Create text chunks
def text_split(processed_file):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(processed_file)

    return text_chunks

#download embedding model
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings