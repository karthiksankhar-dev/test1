import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM

# Set up the Streamlit page configuration
st.set_page_config(page_title="Streaming CS Q&A", layout="centered")
st.title("Computer Science Q&A Assistant (Streaming)")
st.write("Ask any computer science question. The answer will appear in real-time.")

# Define the prompt template for Computer Science queries
# This template guides the model to act as a CS expert.
prompt_template_cs = PromptTemplate(
    template=(
        "You are an AI assistant specializing in computer science. "
        "Provide a detailed and accurate answer to the following question.\n\n"
        "Question: {question}\n\n"
        "Answer:"
    ),
    input_variables=["question"]
)

# Initialize the Ollama LLM
# Ensure the Ollama service is running on your machine.
try:
    model = OllamaLLM(model="llama3.1")
except Exception as e:
    st.error(f"Failed to initialize the Ollama LLM. Please ensure Ollama is running. Error: {e}")
    st.stop()

# Build the chain using LangChain Expression Language (LCEL)
# This modern approach supports streaming out-of-the-box.
chain = prompt_template_cs | model | StrOutputParser()

# Create a text input for the user's question
user_question = st.text_input("Enter your computer science question:", key="question_input")

# If the user has entered a question, stream the response
if user_question:
    st.subheader("Answer:")
    try:
        # Use st.write_stream to display the streaming response
        # The chain.stream() method returns a generator that yields tokens
        stream = chain.stream({"question": user_question})
        st.write_stream(stream)
    except Exception as e:
        st.error(f"An error occurred while generating the response: {e}")
