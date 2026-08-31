# 🏥 Healthcare Monitoring AI Agent

## 📌 Project Overview

The Healthcare Monitoring AI Agent is an AI-powered application that provides general healthcare information to users. It uses **Gemini, LangChain, RAG (Retrieval-Augmented Generation), SQLite, CSV data, and Streamlit**.

Users can ask healthcare-related questions through the Streamlit interface, and the AI agent retrieves relevant information from the medical knowledge base before generating a response.

## 🎯 Objectives

* Provide healthcare-related information using an AI assistant.
* Use RAG to retrieve information from medical documents.
* Provide medicine-related information from a structured dataset.
* Create a simple and user-friendly web interface.
* Organize healthcare data using database and service components.

## ✨ Features

* 🤖 AI Healthcare Assistant
* 📚 RAG-based medical knowledge retrieval
* 💊 Medicine information
* 🗄️ SQLite database support
* 🖥️ Streamlit web interface
* 🔐 Secure API key using environment variables
* ⚠️ Healthcare safety disclaimer

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* Google Gemini
* RAG
* FAISS
* HuggingFace Embeddings
* SQLite
* Pandas
* Git & GitHub

## 📂 Project Structure

```text
Healthcare-Ai-Agent/
│
├── app/
│   ├── agents/
│   │   └── health_agent.py
│   │
│   ├── rag/
│   │   └── vector_store.py
│   │
│   ├── services/
│   │   ├── database.py
│   │   └── medicine_service.py
│   │
│   ├── workflows/
│   │   └── workflow.py
│   │
│   └── main.py
│
├── assets/
│   ├── medicines.csv
│   └── medical documents
│
├── data/
│   └── healthcare.db
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

```text
User
  ↓
Streamlit Interface
  ↓
Healthcare AI Agent
  ↓
RAG retrieves relevant medical information
  ↓
Gemini processes the information
  ↓
Healthcare response
  ↓
User
```

## 📚 RAG System

The RAG system uses medical documents as a knowledge source.

The documents are:

1. Loaded
2. Split into smaller chunks
3. Converted into embeddings
4. Stored in a vector store
5. Searched when the user asks a question
6. Relevant information is provided to the AI agent

This helps the AI generate answers using the project's healthcare knowledge base.

## 💊 Medicine Data

The project contains a medicine dataset with information such as:

* Medicine name
* Purpose
* Strength
* Dosage
* Frequency
* Whether it should be taken after food

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vaidehi-2206/Healthcare-Monitoring-AI-Agent-.git
```

### 2. Open the project

```bash
cd Healthcare-Ai-Agent
```

### 3. Create/activate the virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the API key

Create a `.env` file:

```text
GOOGLE_API_KEY=your_api_key_here
```

Do not upload the `.env` file or API key to GitHub.

### 6. Run the application

```bash
streamlit run app/main.py
```

## 🧪 Example Questions

* What are the symptoms of fever?
* What are the causes of fever?
* What are the symptoms of dehydration?
* What is Crocin used for?

## ⚠️ Disclaimer

This application provides general healthcare information for educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Users should consult a qualified healthcare professional for medical concerns.

## 🔮 Future Improvements

* Patient health monitoring
* Health history tracking
* Appointment reminders
* More medicine and healthcare datasets
* Voice-based interaction
* Improved authentication and user accounts
* Cloud deployment

## 👩‍💻 Project

**Healthcare Monitoring AI Agent**

Developed using Python, LangChain, Gemini, RAG, SQLite, and Streamlit.
