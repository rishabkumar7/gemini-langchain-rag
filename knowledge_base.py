import os

from google.cloud import aiplatform
from langchain_google_vertexai import VertexAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader

from dotenv import load_dotenv

load_dotenv()

embeddings = VertexAIEmbeddings(model_name="text-embedding-005")

"""
List of URLs for the certification knowledge base. This includes the study guides for the most popular cloud certifications:
1. Google Cloud Associate Cloud Engineer
2. Google Cloud Professional Cloud Security Engineer
"""

urls = [
    'https://services.google.com/fh/files/misc/associate_cloud_engineer_exam_guide_english.pdf',
    'https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf',
]

loader = UnstructuredURLLoader(urls)
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)


PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")
BUCKET = os.getenv("BUCKET")
BUCKET_URI = f"gs://{BUCKET}"

# my_index = aiplatform.MatchingEngineIndex.create_tree_ah_index(
#     display_name=DISPLAY_NAME,
#     dimensions=DIMENSIONS,
#     approximate_neighbors_count=150,
#     distance_measure_type="DOT_PRODUCT_DISTANCE",
#     index_update_method="STREAM_UPDATE",  # allowed values # BATCH_UPDATE , STREAM_UPDATE
# )

# Create an endpoint
# my_index_endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
#     display_name=f"{DISPLAY_NAME}-endpoint", # public_endpoint_enabled=True
# )

# NOTE : This operation can take upto 20 minutes
# my_index_endpoint = my_index_endpoint.deploy_index(
#    index=my_index, deployed_index_id=DEPLOYED_INDEX_ID
# )

#my_index_endpoint.deployed_indexes

# TODO : replace 1234567890123456789 with your acutal index ID
my_index = aiplatform.MatchingEngineIndex("8776526113280098304")

# TODO : replace 1234567890123456789 with your acutial endpoint ID
my_index_endpoint = aiplatform.MatchingEngineIndexEndpoint("7252550220624429056")


from langchain_google_vertexai import (
    VectorSearchVectorStore,
    VectorSearchVectorStoreDatastore,
)

vector_store = VectorSearchVectorStoreDatastore.from_components(
    project_id=PROJECT_ID,
    region=REGION,
    index_id=my_index.name,
    endpoint_id=my_index_endpoint.name,
    embedding=embedding_model,
    stream_update=True,
)

vector_store.add_texts(texts=texts, is_complete_overwrite=True)

# Try running a simialarity search
vector_store.similarity_search("Security")