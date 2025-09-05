import os
import logging
import assemblyai as aai

# Configure AssemblyAI API key from environment variables
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

def transcribe_audio_file(file_path: str) -> str:
    """
    Transcribes an audio file using AssemblyAI's API.

    Args:
        file_path (str): The local path to the audio file.

    Returns:
        str: The transcribed text.
    
    Raises:
        Exception: If the transcription fails or the API key is not set.
    """
    if not aai.settings.api_key:
        error_message = "AssemblyAI API key not found in environment variables."
        logging.error(error_message)
        raise Exception(error_message)
    
    try:
        logging.info(f"Starting transcription for {file_path}")
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(file_path)

        if transcript.status == aai.TranscriptStatus.error:
            logging.error(f"AssemblyAI transcription failed: {transcript.error}")
            raise Exception(f"Transcription failed: {transcript.error}")
        
        logging.info("Transcription completed successfully.")
        return transcript.text

    except Exception as e:
        logging.error(f"An unexpected error occurred during transcription: {e}")
        # Re-raise the exception to be handled by the main app
        raise

