AI Voice Agent
This project is a web-based conversational AI agent that you can interact with using your voice. You speak a query, and the agent processes it through a series of cloud services to generate and play back a spoken response, maintaining the context of the conversation.

This application was built as part of the "30 Days of AI Voice Agents" challenge.

Features
Voice-to-Voice Interaction: Simply press a button, speak your query, and receive a spoken answer from the AI.

Conversational Memory: The agent remembers previous turns in the conversation for a given session, allowing for follow-up questions and contextual responses.

Real-time Status Updates: The UI provides clear feedback on the agent's state (e.g., "Listening...", "Thinking...").

Error Handling: Provides a friendly, spoken fallback message if any of the backend services fail.

Custom User Interface: A clean, modern, and friendly UI built with custom CSS, featuring a single, animated button for interaction.

Tech Stack & Architecture
The application follows a client-server architecture, orchestrating several third-party AI services to function.

Technologies Used
Frontend: HTML, CSS, Vanilla JavaScript

Backend: Python with Flask

Speech-to-Text (STT): AssemblyAI

Large Language Model (LLM): Google Gemini

Text-to-Speech (TTS): Murf AI

Architecture Flow
The entire process is handled in a single request-response cycle:

Client: The user records audio in the browser.

Upload: The complete audio file is sent to the Flask backend.

STT: The server sends the audio file to AssemblyAI for transcription.

LLM: The resulting text is appended to the session's chat history and sent to the Google Gemini API to generate a response.

TTS: The text response from Gemini is sent to the Murf AI API to be converted into speech.

Response: The URL of the final audio file is sent back to the client.

Playback: The client's browser plays the received audio URL automatically.

Setup and Installation
Follow these steps to get the project running on your local machine.

1. Clone the Repository
git clone <your-repository-url>
cd language-learning-app

2. Set Up a Python Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Install all the required Python packages using the requirements.txt file.

pip install -r requirements.txt

4. Configure Environment Variables
You need to get API keys from the three services used in this project.

Create a file named .env inside the backend/ directory.

Add your API keys to this file as shown below:

# backend/.env

MURF_API_KEY="your_murf_api_key_here"
ASSEMBLYAI_API_KEY="your_assemblyai_api_key_here"
GOOGLE_API_KEY="your_google_api_key_here"

How to Run
Make sure your virtual environment is activated.

Navigate to the root project directory (language-learning-app).

Run the Flask application:

python backend/app.py

Open your web browser and go to the following URL:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

You should now see the AI Voice Agent interface, ready for you to interact with. A unique session ID will be automatically generated and added to your URL.