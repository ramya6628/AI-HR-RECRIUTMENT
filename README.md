🤖 AI HR Recruitment System

An AI-powered HR Recruitment System that helps recruiters analyze resumes, match candidates with job requirements, and provide intelligent recruitment assistance using Generative AI, LangChain, LangGraph, and RAG.

📌 Project Overview

The AI HR Recruitment System automates important parts of the recruitment process. It can analyze candidate resumes, extract relevant information, compare candidate skills with job requirements, and generate useful recommendations for recruiters.

The system uses Retrieval-Augmented Generation (RAG) to work with recruitment/course-related documents and provides context-aware responses through an AI agent.

✨ Features

📄 Resume Analysis

Extracts candidate information from resumes.

Identifies skills, education, experience, and qualifications.


🎯 Job–Candidate Matching

Compares resume information with job requirements.

Helps identify suitable candidates.


🤖 AI Recruitment Assistant

Provides intelligent responses to recruitment-related queries.

Uses an AI agent for decision support.


🔍 RAG-based Document Search

Processes PDF documents.

Splits documents into meaningful chunks.

Creates vector embeddings.

Retrieves relevant information before generating responses.


🧠 Conversation Memory

Maintains relevant conversation context for better responses.



🛠️ Technologies Used

Technology	Purpose

Python	Backend development
Streamlit	User interface
LangChain	LLM application framework
LangGraph	AI agent workflow
RAG	Context-aware document retrieval
FAISS	Vector database
Gemini	Generative AI / embeddings
PyPDF	PDF document processing


📂 Project Structure

AI-HR-Recruitment/
│
├── agent/
│   ├── graph.py
│   └── ...
│
├── data/
│   └── *.pdf
│
├── services/
│   └── ...
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation

1. Clone the repository

git clone https://github.com/ramya6628/AI-HR-RECRUITMENT.git
cd AI-HR-RECRUITMENT

2. Create virtual environment

python -m venv .venv

3. Activate virtual environment

Windows:

.venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the project root:

GOOGLE_API_KEY=your_api_key_here

Do not upload .env to GitHub. It is already included in .gitignore.

▶️ Run the Application

streamlit run app.py

The application will open in your browser.

🔄 RAG Workflow

PDF Documents
      ↓
PDF Loader
      ↓
Text Splitting
      ↓
Google Embeddings
      ↓
FAISS Vector Store
      ↓
Relevant Document Retrieval
      ↓
Gemini LLM
      ↓
AI Response

🎯 Objective

The main objective of this project is to build an intelligent recruitment assistant that reduces manual resume screening, improves candidate matching, and provides faster AI-assisted recruitment decisions.

🚀 Future Enhancements

Candidate ranking system

Automated interview question generation

Interview scheduling

Email notification system

Advanced candidate scoring

Database integration

Recruiter dashboard

Deployment to cloud


---

Note: Never commit API keys, passwords, .env files, or the .venv folder to GitHub.
