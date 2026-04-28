# 📄 AI-Powered Policy Documentation Navigator

An intelligent Streamlit-based application that allows users to upload long policy documents (PDFs) and ask natural language questions to receive structured, bullet-point answers instantly.

Built as part of the Gen AI Challenge 🚀

---

## 🚀 Problem Statement

Government and institutional policy documents are often long, complex, and difficult to navigate.  
Users spend significant time searching for specific information within large PDFs.

There is a need for an intelligent tool that can:
- Extract relevant information quickly
- Answer natural language questions
- Present results in a structured and readable format

---

## 💡 Solution

The Policy Documentation Navigator enables users to:

- Upload PDF policy documents
- Automatically clean and process the text
- Ask questions in natural language
- Receive concise bullet-point answers
- View query history
- Get optimized performance for large documents

---

## ✨ Key Features

- 📂 PDF Upload & Text Extraction
- 🧹 Smart Text Cleaning (removes spacing errors like "F ormerly")
- ⚡ Performance Optimization (30,000 character limit for speed)
- 🔍 Keyword-Based Intelligent Sentence Scoring
- 📌 Bullet-Point Answer Formatting
- 📜 Query History Tracking
- 🎨 Clean Dark-Themed UI

---

## 🏗️ System Architecture

User  
⬇  
Upload PDF  
⬇  
Text Extraction (PyPDF2)  
⬇  
Text Cleaning (Regex Processing)  
⬇  
Sentence Splitting  
⬇  
Question Input  
⬇  
Sentence Scoring Algorithm  
⬇  
Top Relevant Sentences  
⬇  
Bullet-Point Answer Display  

---

## 🛠️ Tech Stack

- Python
- Streamlit
- PyPDF2
- Regular Expressions (Regex)
- Streamlit Session State

---

## ⚡ Performance Optimization

To ensure faster response times for large documents:

- Text cleaning reduces noise
- Document limited to first 30,000 characters
- Pre-splitting sentences stored in session state
- Stopword removal improves scoring efficiency

---

## 📦 Installation & Setup

1️⃣ Clone the repository:

```bash
git clone https://github.com/sonalee-Desg/scaledown.git
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Run the application:

```bash
streamlit run app_ui.py
```

---

## 🌟 Creative Feature

The application includes an optimized text-processing and structured answer formatting system that:

- Automatically cleans noisy PDF text
- Converts extracted answers into readable bullet points
- Maintains interactive query history
- Improves speed using controlled document size

This improves usability compared to manually searching through long policy documents.

---

## ⭐ Creative Feature

### 📊 Answer Confidence Scoring

The system calculates a relevance score based on keyword matching and displays a confidence percentage for each response.

This provides users with transparency on how strongly the retrieved sentences match the query.


## 🔮 Future Improvements

- Semantic Search using Embeddings
- Retrieval-Augmented Generation (RAG)
- LLM Integration (OpenAI / HuggingFace)
- PDF Highlighting of Answers
- Chat-style conversational interface
- Cloud Deployment

---

## 🤖 AI Assistance Disclosure

This project was developed using AI as a collaborative development assistant.

AI tools were used extensively for:
- Code generation and refinement
- Debugging support
- Structuring the application architecture
- Improving performance optimization
- Writing documentation

All code was reviewed, tested, modified, and integrated by the author.  
The project reflects hands-on understanding of how the components work together, including PDF processing, text cleaning, sentence scoring, and Streamlit session management.

The AI was used as a productivity and learning accelerator throughout the development process.


## 👩‍💻 Author

**Sonali Maity**  
Built for the Gen AI Challenge 🚀

location / {

proxy_pass http://localhost:4000;

proxy_http_version 1.1;

proxy_set_header Upgrade $http_upgrade;

proxy_set_header Connection 'Upgrade';

proxy_set_header Host $host;

proxy_cache_bypass $http_upgrade;

}
