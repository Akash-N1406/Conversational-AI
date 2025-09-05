# 🎙️ AI Voice Agent

A **web-based conversational AI agent** that allows you to interact with artificial intelligence using your **voice**.  
Speak a query, let the AI process it, and hear the spoken response — all while maintaining conversational context.

This project was built as part of the **"30 Days of AI Voice Agents" challenge**.

---

## ✨ Features
- 🎤 **Voice-to-Voice Interaction**: Press a button, speak, and get an AI-generated spoken response.
- 🧠 **Conversational Memory**: Maintains context across turns within a session for natural conversations.
- 🔄 **Real-time Status Updates**: Clear feedback states (e.g., *Listening...*, *Thinking...*).
- 🛡️ **Error Handling**: Friendly fallback messages if backend services fail.
- 🎨 **Custom UI**: Clean and modern single-button interface with animations.

---

## 🏗️ Tech Stack & Architecture

### Frontend
- **HTML, CSS, Vanilla JavaScript**

### Backend
- **Python (Flask)**

### Cloud Services
- **Speech-to-Text (STT):** [AssemblyAI](https://www.assemblyai.com/)  
- **Large Language Model (LLM):** [Google Gemini](https://ai.google.dev/)  
- **Text-to-Speech (TTS):** [Murf AI](https://murf.ai/)  

---

## 🔄 Architecture Flow
1. **Client:** User records audio in the browser.  
2. **Upload:** Audio file is sent to Flask backend.  
3. **STT:** Backend sends audio to AssemblyAI for transcription.  
4. **LLM:** Transcript is appended to chat history and sent to Google Gemini for response generation.  
5. **TTS:** Gemini’s text response is converted to speech using Murf AI.  
6. **Response:** Backend sends audio URL to the client.  
7. **Playback:** Browser automatically plays the generated speech.  

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd language-learning-app

2. Create a Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file inside the backend/ directory with your API keys:

# backend/.env
MURF_API_KEY="your_murf_api_key_here"
ASSEMBLYAI_API_KEY="your_assemblyai_api_key_here"
GOOGLE_API_KEY="your_google_api_key_here"

🚀 Running the Application

Make sure your virtual environment is activated, then:

cd language-learning-app
python backend/app.py


Open your browser at:
👉 http://127.0.0.1:5000

A unique session ID will be generated and appended to your URL.

📂 Project Structure
language-learning-app/
│── backend/
│   ├── app.py          # Flask server
│   ├── requirements.txt
│   └── .env            # API keys
│
│── frontend/
│   ├── index.html      # Main UI
│   ├── styles.css      # Custom styles
│   └── script.js       # Client-side logic
│
└── README.md

🙌 Acknowledgments

AssemblyAI
 for Speech-to-Text

Google Gemini
 for conversational AI

Murf AI
 for Text-to-Speech
