import os

from langchain.prompts import PromptTemplate
from google.cloud import aiplatform
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_google_community import BigQueryVectorStore

from dotenv import load_dotenv
load_dotenv()


embedding = VertexAIEmbeddings(model_name="text-embedding-005")

vector_store = BigQueryVectorStore(
    project_id=os.getenv("PROJECT"),
    dataset_name=os.getenv("DATASET"),
    table_name=os.getenv("TABLE"),
    location=os.getenv("REGION"),
    embedding=embedding,
)


def ai_helper(query):
  llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
  )

  docs = vector_store.similarity_search(query)
  docs = " ".join([d.page_content for d in docs])

  prompt=PromptTemplate(
    input_variable = ["question","docs"],
    template = """
    You are a helpful assistant that can answer questions and concerns about Google Cloud Certifications. You can help users with questions about the certification process, exam details, and project ideas. You can also provide information about the different certification paths and the benefits of getting certified. Answer the user's {question} based on the information provided here {docs}"""
  )


  chain = prompt | llm
  response = chain.invoke({"question":query,"docs":docs})
  return response

print(ai_helper("How can I pass Associate Cloud Engineer exam?"))