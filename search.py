import os

from google.cloud import aiplatform
from langchain_google_vertexai import VertexAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_google_community import BigQueryVectorStore

from dotenv import load_dotenv

load_dotenv()

embedding = VertexAIEmbeddings(model_name="text-embedding-005")

PROJECT_ID = os.getenv("PROJECT")
REGION = os.getenv("REGION")
DATASET= os.getenv("DATASET")
TABLE = os.getenv("TABLE")

vector_store = BigQueryVectorStore(
    project_id=PROJECT_ID,
    dataset_name=DATASET,
    table_name=TABLE,
    location=REGION,
    embedding=embedding,
)

search = vector_store.similarity_search("Security")
print(f"here are the docs searched {search}")