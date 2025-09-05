from murf.client import Murf
import os

# Initialize the Murf client with the API key
murf_client = Murf(api_key=os.getenv("MURF_API_KEY"))

def generate_tts_audio(text: str) -> str:
    """
    Generates audio from text using the Murf AI API.

    Args:
        text (str): The text to be converted to speech.

    Returns:
        str: The URL of the generated audio file.
        
    Raises:
        Exception: If the TTS generation fails.
    """
    try:
        # CORRECTED: Use the text_to_speech.generate method as per SDK docs
        response = murf_client.text_to_speech.generate(
            text=text,
            voice_id="en-US-natalie",
            # Parameters like format and sample_rate can be added here if needed
        )
        # CORRECTED: Access the URL via the .audio_file attribute
        return response.audio_file
    except Exception as e:
        print(f"An error occurred in generate_tts_audio: {e}")
        raise

