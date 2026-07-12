# 🎓 AI Placement Preparation System

An AI-powered multi-agent learning platform designed to help students prepare for technical placements through personalized teaching, interview preparation, quizzes, roadmap generation, and resume guidance.

> 🚧 This project is currently under active development.

---

## 🚀 Features

### ✅ Teacher Agent (Completed)
- Personalized explanations based on student level
- Multiple learning modes
  - 📘 Learning Mode
  - 📝 Notes Mode
  - 💼 Interview Mode
  - 🔄 Comparison Mode (Coming Soon)
  - 💻 Coding Mode (Coming Soon)
- Step-by-step explanations
- Interview-focused teaching
- Real-world examples
- Beginner to Advanced support

---

## 🤖 Upcoming Agents

- 🎯 Quiz Agent
- 📅 Study Planner Agent
- 📄 Resume Review Agent
- 💬 Interview Simulator
- 🧠 Progress Tracker
- 📚 Roadmap Generator

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | LangChain |
| LLM | Google Gemini 2.5 Flash |
| Prompting | ChatPromptTemplate |
| Output Parsing | StrOutputParser |
| Environment | python-dotenv |

---

## 📁 Project Structure

```text
project/
│
├── app.py
│
├── Agents/
│   └── teacher_agent.py
│
├── Prompt/
│   └── Teacher_prompt.py
│
├── llms/
│   └── gemini.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation



### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

### Run the Project

```bash
python app.py
```

---

## 🧩 Current Workflow

```text
User
   │
   ▼
Teacher Agent
   │
   ▼
Prompt Template
   │
   ▼
Gemini 2.5 Flash
   │
   ▼
Formatted Educational Response
```

---

## 📖 Example

Input

```
Goal: Become AI Engineer

Mode: Learning

Level: Beginner

Question:

Explain LangGraph.
```

Output

- Definition
- Working
- Real-world Example
- Code Example
- Interview Questions
- Practice Questions
- Summary

---

## 🎯 Future Improvements

- [ ] Prompt Routing
- [ ] LangGraph Integration
- [ ] RAG Support
- [ ] Vector Database
- [ ] Chat Memory
- [ ] Voice Assistant
- [ ] PDF Notes Generator
- [ ] Study Analytics Dashboard
- [ ] Web UI (Streamlit/Gradio)

---

## 📌 Learning Goals

This project is being developed to improve skills in:

- LangChain
- Prompt Engineering
- Multi-Agent AI Systems
- LLM Application Development
- AI Product Design
- Python

---



## 👨‍💻 Author

**Aman Raj**

IIMT college of engineering , Greater Noida
B.Tech (AI & DS)


GitHub: https://github.com/goluraj120/Agentic_AI

LinkedIn: https://www.linkedin.com/in/aman-raj-600904280