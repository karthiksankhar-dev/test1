<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# import streamlit as st

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM

# Set up the Streamlit page configuration

st.set_page_config(page_title="Streaming CS Q\&A", layout="centered")
st.title("Computer Science Q\&A Assistant (Streaming)")
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
        \# Use st.write_stream to display the streaming response
        \# The chain.stream() method returns a generator that yields tokens
        stream = chain.stream({"question": user_question})
        st.write_stream(stream)
    except Exception as e:
        st.error(f"An error occurred while generating the response: {e}")

Now I would like to add the above code to my github repo. The above code has the llama model. But the others access the repository how will they able to make the setup to execute the above code file

To help others execute your code after cloning your GitHub repository, you should provide a `README.md` file with clear, step-by-step setup instructions. This file will guide them through installing the necessary software, setting up the environment, and running the application.

Here is a template for your `README.md` file that you can add to your repository.

***

# Computer Science Q\&A Assistant

This project is a web-based Q\&A application built with Streamlit that uses a local large language model (LLM) via Ollama to answer computer science questions.

## How It Works

The application provides a simple web interface where a user can enter a computer science-related question. The query is sent to a locally running Llama 3.1 model, and the answer is streamed back in real-time.

### Core Technologies

* **Streamlit**: For creating the web application interface.
* **LangChain**: For building the application logic and connecting to the language model.
* **Ollama**: For serving the `llama3.1` model locally on your machine.


## Prerequisites

Before you begin, ensure you have the following installed on your system:

* **Python 3.8 or newer**: You can download it from [python.org](https://www.python.org/downloads/).
* **Ollama**: You must install Ollama to run the language model locally. Download it from [ollama.com](https://ollama.com).


## Setup Instructions

Follow these steps to set up and run the project on your local machine.

### Step 1: Clone the Repository

First, clone this repository to your local machine using Git:

```bash
git clone <your-repository-url>
cd <your-repository-directory>
```


### Step 2: Create a `requirements.txt` File

Create a file named `requirements.txt` in the root of your project directory and add the following lines to it. This file lists all the Python dependencies needed to run the script.

```text
streamlit
langchain-core
langchain-ollama
```


### Step 3: Set Up a Python Virtual Environment

It is highly recommended to create a virtual environment to manage project-specific dependencies.

**On macOS/Linux:**

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

**On Windows:**

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate
```


### Step 4: Install Dependencies

With your virtual environment activated, install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```


### Step 5: Download and Run the Ollama Model

Before running the application, you need to have the Ollama service running and the `llama3.1` model downloaded.

1. **Start the Ollama Application**: Launch the Ollama application that you installed during the prerequisite step.
2. **Pull the Model**: Open your terminal and run the following command to download the `llama3.1` model. This may take some time depending on your internet connection.

```bash
ollama pull llama3.1
```

Once the download is complete, leave the Ollama service running in the background.

### Step 6: Run the Streamlit Application

Finally, you can run the Python script. Make sure your terminal is in the project's root directory and your virtual environment is active.

```bash
streamlit run your_script_name.py
```

Replace `your_script_name.py` with the actual name of your Python file.

After running the command, your web browser should open a new tab with the Streamlit application running. You can now ask a computer science question and see the response generated in real-time.

