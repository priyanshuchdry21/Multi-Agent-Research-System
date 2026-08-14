# 🔬 ResearchMind – Multi-Agent AI Research System

> AI-powered autonomous research assistant built with **LangGraph, LangChain, Streamlit, and Large Language Models (LLMs)**.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-AI-green?style=for-the-badge)
![LangGraph](https://img.shields.io/badge/LangGraph-MultiAgent-orange?style=for-the-badge)
![LLM](https://img.shields.io/badge/LLM-Gemini%20%7C%20Groq-purple?style=for-the-badge)

---

## 📖 Overview

ResearchMind is an **AI-powered Multi-Agent Research System** that automates the complete research workflow.

Instead of relying on a single LLM prompt, the application coordinates multiple specialized AI agents that work together to search, analyze, summarize, and review information before generating a polished research report.

The project demonstrates how **Multi-Agent AI Systems** can solve complex tasks using collaborative reasoning.

---

## 🚀 Features

- 🔍 AI Search Agent
- 📄 Intelligent Web Reader Agent
- ✍️ AI Writer Agent
- 🧐 AI Critic Agent
- 📑 Automatic Research Report Generation
- ⚡ Modern Streamlit UI
- 🤖 Gemini & Groq LLM Support
- 🔄 Multi-Agent Workflow using LangGraph
- 📥 Download Research Report
- 🎯 Structured AI Pipeline

---

# 🧠 Multi-Agent Workflow

```text
User Query
     │
     ▼
Search Agent
     │
     ▼
Reader Agent
     │
     ▼
Writer Agent
     │
     ▼
Critic Agent
     │
     ▼
Final Research Report
```

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | User Interface |
| LangChain | LLM Framework |
| LangGraph | Multi-Agent Workflow |
| Gemini API | Large Language Model |
| Groq API | Alternative LLM |
| Tavily Search | Web Search |
| BeautifulSoup | Web Scraping |

---

# 📂 Project Structure

```text
ResearchMind/
│
├── app.py
├── agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .gitignore
├── tests/
│     └── test_agents.py
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/priyanshuchdry21/Multi-Agent-Research-System.git
```

Move into the project

```bash
cd Multi-Agent-Research-System
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

Example

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
