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
git clone https://github.com/karthiksankhar-dev/test1.git
cd test1
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
streamlit run code.py
```

Replace `code.py` with the actual name of your Python file.

After running the command, your web browser should open a new tab with the Streamlit application running. You can now ask a computer science question and see the response generated in real-time.

