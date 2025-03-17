# Gemini LangChain Rag

A demo project to build a Google Cloud Certifications Chatbot using Langchain, Google Cloud AI Platform, and Vertex AI. The project demonstrates how to:

- Load and split certification study guides from URLs.
- Create vector embeddings using Vertex AI.
- Store and search document embeddings in BigQuery.
- Interface with a generative AI model for answering user queries.
- Run a web demo with [Streamlit](https://streamlit.io).

![Gemini LangChain RAG Architecture](https://storage.googleapis.com/rishabincloud/gemini-langchain-vertexai-rag.png)

## Project Structure

- **[ai.py](ai.py)**: Contains the AI helper function that integrates the language model and document similarity search to answer certification questions.
- **[knowledge_base.py](knowledge_base.py)**: Loads certification study guides, splits them into chunks, and adds them to the BigQuery vector store.
- **[search.py](search.py)**: Demonstrates running a similarity search on the vector store.
- **[vertexai_vectorsearch.py](vertexai_vectorsearch.py)**: An alternative example implementing vector search with Vertex AI’s matching engine.
- **[streamlit.py](streamlit.py)**: Runs a Streamlit web demo for interacting with the chatbot.
- **.env**: Environment configuration file for setting project-specific variables.
- **[requirements.txt](requirements.txt)**: Lists the dependencies for the project.

## Prerequisites

- Python 3.9+
- A Google Cloud Project with AI Platform and BigQuery enabled.
- Proper service account credentials configured for accessing Google Cloud resources.

## Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/rishabkumar7/gemini-langchain-rag
   cd gemini-langchain-rag
   ```

2. **Configure Environment Variables**
   - Copy the example file and modify the values:
     ```sh
     cp .env.example .env
     ```
   - Update the `.env` file with your Google Cloud project ID, dataset, table, region, and API key.

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Demo

### Command Line Execution

- **Knowledge Base Loading**  
  Run [knowledge_base.py](knowledge_base.py) to load and add certification documents to the vector store.
  ```sh
  python knowledge_base.py
  ```

- **Vector Search Example**  
  Run [search.py](search.py) or [vertexai_vectorsearch.py](vertexai_vectorsearch.py) to test the vector search functionality.
  ```sh
  python search.py
  # or
  python vertexai_vectorsearch.py
  ```

- **Chatbot AI Helper**  
  The [ai.py](ai.py) file invokes the AI helper function with a sample query. You can modify the code to test different questions.

### Web Demo with Streamlit

Launch the web-based chatbot interface provided by [streamlit.py](streamlit.py):
```sh
streamlit run streamlit.py
```
Access the local URL provided by Streamlit to interact with the chatbot.

## License

This project is licensed under the [MIT License](LICENSE).

## Additional Information

- Ensure you have set up proper cloud credentials as outlined in Google Cloud’s documentation.
- For more details on Langchain integration with Google Vertex AI, refer to Langchain’s official docs.

Enjoy exploring Google Cloud Certifications with gemini-langchain-rag!

## Author

- Twitter: [@rishabincloud](https://x.com/rishabincloud)
- LinkedIn: [rishabkumar7](https://linkedin.com/in/rishabkumar7)
