from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import logging
import uuid
from werkzeug.utils import secure_filename

# Import the service modules
from services import stt_service, llm_service, tts_service

# Load environment variables
load_dotenv()

# --- App Initialization and Logging ---
app = Flask(__name__, template_folder='templates', static_folder='static')

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

# --- In-Memory Storage ---
chat_histories = {} # Simple in-memory storage for chat histories

# --- File Upload Configuration ---
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- HTTP Route Definitions ---

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/api/agent/chat/<session_id>', methods=['POST'])
def agent_chat(session_id):
    """
    Handles the main conversational agent logic via file upload.
    """
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    filename = secure_filename(f"{uuid.uuid4()}.webm")
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    audio_file.save(audio_path)
    logging.info(f"Audio file saved at {audio_path}")

    try:
        # 1. Transcribe Audio
        user_transcript = stt_service.transcribe_audio_file(audio_path)
        logging.info(f"[{session_id}] User said: {user_transcript}")

        # 2. Manage Chat History
        if session_id not in chat_histories:
            chat_histories[session_id] = []
        chat_histories[session_id].append({"role": "user", "parts": [user_transcript]})
        
        # 3. Get LLM Response
        llm_response_text = llm_service.get_llm_response(chat_histories[session_id])
        logging.info(f"[{session_id}] LLM responded: {llm_response_text}")
        chat_histories[session_id].append({"role": "model", "parts": [llm_response_text]})
        
        # 4. Convert Response to Speech
        response_audio_url = tts_service.generate_tts_audio(llm_response_text)
        
        return jsonify({"audioUrl": response_audio_url, "isError": False})

    except Exception as e:
        logging.error(f"An error occurred in agent_chat: {e}", exc_info=True)
        fallback_text = "I'm having some trouble right now. Please try again in a moment."
        
        try:
            fallback_audio_url = tts_service.generate_tts_audio(fallback_text)
            return jsonify({"audioUrl": fallback_audio_url, "isError": True}), 500
        except Exception as fallback_e:
            logging.error(f"Failed to generate fallback audio: {fallback_e}", exc_info=True)
            return jsonify({"error": "A critical error occurred on the server."}), 500
            
    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

