# 🎓 AI Learning Assistant

An AI-powered multi-agent learning platform built with **LangChain**, **Google Gemini**, and **Streamlit** to provide personalized educational assistance. The project helps students learn technical concepts, prepare for interviews, generate notes, compare technologies, solve coding problems, and much more.

> 🚧 This project is actively under development. New AI agents and learning features are being added continuously.

---

# ✨ Features

## ✅ Teacher Agent (Completed)

The Teacher Agent provides personalized learning based on the user's goal, knowledge level, preferred language, and learning mode.

### 📚 Supported Learning Modes

- 📘 Learning Mode
  - Beginner to advanced explanations
  - Step-by-step teaching
  - Real-world examples

- 📝 Notes Mode
  - Short and structured notes
  - Revision-friendly content
  - Key points and summaries

- 💼 Interview Mode
  - Interview-oriented explanations
  - Frequently asked interview questions
  - Tips and best practices

- ⚖️ Compare Mode
  - Compare two technologies or concepts
  - Advantages & disadvantages
  - Use cases
  - Feature comparison

- 💻 Coding Mode
  - Code generation
  - Code explanation
  - Debugging assistance
  - Best practices

---

## ✅ Quiz Agent (Completed)

The Quiz Agent generates personalized quizzes based on the user's learning goal, topic, knowledge level, and preferred language. It helps users evaluate their understanding through interactive multiple-choice questions.

### 📝 Features

* 🎯 Personalized Quiz Generation

  * Topic-based quizzes
  * Goal-oriented questions
  * Difficulty-based question selection
  * Language support

* ❓ Multiple Choice Questions (MCQs)

  * 10 automatically generated questions
  * Four options (A, B, C, D)
  * One correct answer
  * Concept-based questions

* 📊 Quiz Evaluation

  * Automatic score calculation
  * Marks for each question
  * Final score summary
  * Performance feedback

* 💡 Answer Explanation

  * Correct answer after submission
  * Short explanation for every question
  * Helps reinforce learning

* 🧠 Structured Output

  * Pydantic schema validation
  * Reliable structured quiz generation
  * Consistent output format
  * Easy integration with Streamlit UI

---


# 🚀 Upcoming Agents

- 🛣️ Roadmap Agent
- 📄 Resume Review Agent
- 📅 Study Planner Agent
- 💬 Mock Interview Agent
- 📚 PDF Notes Generator
- 🧠 Progress Tracker
- 📂 RAG-based Document Assistant
- 🎤 Voice Learning Assistant

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | LangChain |
| LLM | Google Gemini 2.5 Flash |
| UI | Streamlit |
| Prompting | ChatPromptTemplate |
| Output Parser | StrOutputParser |
| Environment | python-dotenv |

---

# 📂 Project Structure

```text
AI_Learning_Assistant/
│
├── app.py
├── UI/
│   ├──Quiz_ui.py
|   └──Teacher_ui.py
|
├── Agents/
│   ├── teacher_agent.py
│   └── quiz_agent.py
|
├── Prompt/
|   └── Teacher_prompt/ 
│     ├── prompt_router.py
│     ├── learning_prompt.py
│     ├── notes_prompt.py
│     ├── interview_prompt.py
│     ├── compare_prompt.py
│     └── coding_prompt.py
│   └── Quiz_prompt.py
|   └── prompt_router.py
|
├── llms/
│   └── gemini.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/goluraj120/Agentic_AI.git

cd Agentic_AI
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Run the Application

```bash
streamlit run app.py
```

---

# 🧩 Current Workflow

```text
                            User
                             │
                             ▼
                        Streamlit UI
                 ┌─────────────┼─────────────┐
                 ▼                           ▼
              Teacher Agent              Quiz_Agent
                    │                         │
                    ▼                         ▼ 
             Prompt Router               Gemini 2.5 Flash
                    │                           │
      ┌─────────────┼─────────────┐             ▼
      ▼             ▼             ▼      Personalized Response
 Learning      Interview      Notes
      │
      ▼
  Gemini 2.5 Flash
      │
      ▼
 Personalized Response
```                          
                                            
                                                 
                                         
                   

---

# 📖 Example

### Input

```text
Goal      : Become AI Engineer

Mode      : Learning

Level     : Beginner

Language  : English

Question  : Explain LangGraph.
```

### Output

- Concept Explanation
- Step-by-Step Breakdown
- Real-world Example
- Interview Questions
- Practice Questions
- Summary

---

# 🎯 Future Roadmap

- [x] Teacher Agent
- [x] Prompt Router
- [x] Multiple Learning Modes
- [x] Quiz Agent
- [ ] Roadmap Generator
- [ ] Resume Review Agent
- [ ] Study Planner
- [ ] Mock Interview
- [ ] RAG Integration
- [ ] Vector Database
- [ ] Memory Support
- [ ] Voice Assistant
- [ ] PDF Export
- [ ] User Authentication
- [ ] Chat History

---

# 🎯 Learning Objectives

This project is being developed to strengthen practical skills in:

- Prompt Engineering
- LangChain
- Multi-Agent AI Systems
- LLM Application Development
- AI Product Design
- Streamlit
- Python
- Agentic AI

---


# 👨‍💻 Author

**Aman Raj**

B.Tech (Artificial Intelligence & Data Science)

IIMT College of Engineering, Greater Noida

### GitHub

https://github.com/goluraj120/Agentic_AI

### LinkedIn

https://www.linkedin.com/in/aman-raj-600904280

