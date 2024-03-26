from src.helper import file, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get('API_KEY')
INDEXES_ENVIRONMENT = os.environ.get('INDEXES_ENVIRONMENT')

processed_file = file("database/")
text_chunks = text_split(processed_file)
embeddings = download_hugging_face_embeddings()

#Initializing the Pinecone
pinecone.init(api_key=API_KEY,
              environment=INDEXES_ENVIRONMENT)

index_name="chatbot"

#Creating Embeddings for Each of The Text Chunks & storing
docsearch=Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)