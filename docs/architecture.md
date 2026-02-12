# 📐 Project Documentation – System Architecture

## 1. Project Overview

The AI-Powered Policy Documentation Navigator is a retrieval-based document question-answering system built using Streamlit.

It allows users to upload PDF policy documents and ask natural language questions. The system processes the document and retrieves relevant answers in structured bullet-point format.

---

## 2. System Workflow

The system follows this processing pipeline:

1. User uploads PDF
2. PDF is processed using PyPDF2
3. Raw text is extracted from pages
4. Text cleaning is applied using regular expressions
5. Document is limited to 30,000 characters for performance
6. Text is split into sentences
7. User submits a question
8. Stopwords are removed from the question
9. Sentence scoring algorithm calculates relevance
10. Top 5 relevant sentences are selected
11. Results are formatted into bullet points
12. Answer is displayed in the UI

---

## 3. Text Cleaning Strategy

PDF documents often contain:
- Broken words (e.g., "F ormerly")
- Extra spacing
- Irregular punctuation formatting

Cleaning improvements include:

- Regex merging of split characters
- Removal of extra whitespace
- Correction of punctuation spacing

This improves readability and retrieval accuracy.

---

## 4. Sentence Scoring Algorithm

The retrieval logic works as follows:

- Convert question to lowercase
- Remove stopwords
- Extract meaningful keywords
- Compare each sentence with question keywords
- Assign score based on keyword matches
- Rank sentences by score
- Select top 5 sentences

This creates a lightweight retrieval-based question-answering system.

---

## 5. Performance Optimization

To improve speed:

- Document is limited to first 30,000 characters
- Sentences are precomputed and stored in session state
- Stopwords reduce unnecessary matching
- No repeated PDF parsing per query

This ensures smoother UI experience even for large policy documents.

---

## 6. Limitations

- Keyword-based retrieval (not semantic search)
- No contextual memory between queries
- Limited to PDF input format
- No embedding-based similarity search

---

## 7. Future Enhancement Plan

- Integrate semantic embeddings (FAISS / sentence-transformers)
- Add Retrieval-Augmented Generation (RAG)
- Integrate LLM for contextual summarization
- Add answer confidence scoring
- Deploy on Streamlit Cloud

---
