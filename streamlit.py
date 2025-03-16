import streamlit as st
import ai as ai
import textwrap


st.title("Google Cloud Certifications Chatbot")
st.write("This chatbot can help you with questions about Google Cloud Certifications. It can answer questions about the certification process, exam details, and project ideas. It can also provide information about the different certification paths and the benefits of getting certified.")

query = st.text_input("Ask a question about Google Cloud Certifications")
if query:
    response = ai.ai_helper(query)
    st.write(response)