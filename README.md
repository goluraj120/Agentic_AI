# 🎓 AI Learning Assistant

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Agentic%20AI-green)
![Gemini](https://img.shields.io/badge/Google-Gemini-red)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-blue)

</p>

An AI-powered **Multi-Agent Learning Platform** built with **LangChain**, **Google Gemini**, **Groq**, and **Streamlit**. The project helps students learn technical concepts, generate quizzes, create study plans, build ATS-friendly resumes, and chat with YouTube videos using AI.

---

# ✨ Features

- 📚 Teacher Agent
- 📝 Quiz Agent
- 📅 Planner Agent
- 📄 Resume Builder Agent
- 🎥 YouTube Chatbot Agent
- 🤖 Multi-Agent Architecture
- 🎯 Personalized Learning
- 📋 Structured Outputs using Pydantic
- 💻 Interactive Streamlit UI

---

# 🤖 Teacher Agent

The Teacher Agent provides personalized learning experiences based on the user's learning goal, level, language, and selected mode.

### Features

- Learning Mode
- Notes Mode
- Interview Mode
- Compare Mode
- Coding Mode
- Step-by-step explanations
- Real-world examples
- Interview preparation
- Code generation and debugging

---

# 📝 Quiz Agent

Generates personalized quizzes to evaluate learning.

### Features

- Topic-based MCQs
- Difficulty Levels
- Automatic Evaluation
- Score Calculation
- Answer Explanation
- Structured Quiz Schema
- Pydantic Validation

---

# 📅 Planner Agent

Creates personalized study plans based on the user's goals.

### Features

- Weekly Study Plan
- Learning Objectives
- Revision Schedule
- Daily Tasks
- Quiz Recommendations
- Time Allocation
- Goal-Based Roadmaps

---

# 📄 Resume Builder Agent

An AI-powered ATS-friendly Resume Assistant.

### Features

- ATS-Friendly Resume
- Professional Summary
- AI Skill Suggestions
- Resume Templates
  - Fresher
  - AI Engineer
  - Software Engineer
  - Data Scientist
- Project Enhancement
- Action Verb Optimization
- Structured Resume Schema

---

# 🎥 YouTube Chatbot Agent

Allows users to ask questions from any YouTube video's transcript using RAG.

### Features

- Transcript Retrieval
- Gemini Embeddings
- ChromaDB Vector Store
- Context Retrieval
- Transcript-Based Answers
- Natural Language Questions

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | LangChain |
| LLM | Google Gemini, Groq |
| UI | Streamlit |
| Vector DB | ChromaDB |
| Embeddings | Gemini Embeddings |
| Prompting | ChatPromptTemplate |
| Validation | Pydantic |
| Environment | python-dotenv |

---

# 📂 Project Structure

```text
AI_Learning_Assistant/
│
├── app.py
│
├── Agents/
│   ├── teacher_agent.py
│   ├── quiz_agent.py
│   ├── planner_agent.py
│   ├── resume_agent.py
│   └── youtube_agent.py
│
├── Prompt/
│   ├── Teacher_prompt/
│   ├── quiz_prompt.py
│   ├── planner_prompt.py
│   ├── resume_prompt.py
│   ├── youtube_prompt.py
│   └── prompt_router.py
│
├── Schema/
│   ├── quiz_schema.py
│   ├── planner_schema.py
│   └── resume_schema.py
│
├── Templates/
│   ├── fresher.py
│   ├── ai_engineer.py
│   ├── software_engineer.py
│   └── data_scientist.py
│
├── UI/
│   ├── Teacher_UI.py
│   ├── Quiz_UI.py
│   ├── planner_UI.py
│   ├── resume_UI.py
│   └── Youtube_UI.py
│
├── llms/
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/goluraj120/Agentic_AI.git

cd Agentic_AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add API Key

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

### Run

```bash
streamlit run app.py
```

---

# 🚀 Usage

1. Launch Streamlit.
2. Select an AI Agent.
3. Enter your inputs.
4. Generate AI responses.
5. Learn, practice, plan, or build your resume.

---

# 🏗 Architecture

```text
                    User
                      │
                      ▼
                 Streamlit UI
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 Teacher Agent   Quiz Agent     Planner Agent
      │               │               │
      ├───────────────┼───────────────┤
                      ▼
             Resume Builder Agent
                      │
                      ▼
            YouTube Chatbot Agent
                      │
                      ▼
             Google Gemini / Groq
```

---

# 🔄 Workflow

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Selected Agent
 │
 ▼
Prompt
 │
 ▼
Gemini / Groq
 │
 ▼
Pydantic Parser
 │
 ▼
Structured Response
 │
 ▼
Streamlit Output
```

---

# 📸 Screenshots

Add screenshots here.

```text
screenshots/
├── home.png
├── teacher.png
├── quiz.png
├── planner.png
├── resume.png
└── youtube.png
```

---

# 🗺 Future Roadmap

- ✅ Teacher Agent
- ✅ Quiz Agent
- ✅ Planner Agent
- ✅ Resume Builder Agent
- ✅ YouTube Chatbot Agent
- ⏳ Mock Interview Agent
- ⏳ Cover Letter Generator
- ⏳ PDF Resume Export
- ⏳ Progress Tracker
- ⏳ Voice Assistant
- ⏳ Authentication

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 👨‍💻 Author

**Aman Raj**

**B.Tech (AI & DS)**

IIMT College of Engineering, Greater Noida

GitHub: https://github.com/goluraj120/Agentic_AI

LinkedIn: https://www.linkedin.com/in/aman-raj-600904280

---

# 📜 License

This project is licensed under the **MIT License**.

---

⭐ **If you found this project helpful, don't forget to star the repository!**