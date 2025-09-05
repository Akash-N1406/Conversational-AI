import google.generativeai as genai
import os

# Configure the Gemini client with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

def get_llm_response(chat_history: list) -> str:
    """
    Generates a response from the Gemini LLM based on chat history.

    Args:
        chat_history (list): A list of dictionaries representing the conversation.

    Returns:
        str: The text response from the LLM.
        
    Raises:
        Exception: If the LLM call fails.
    """
    try:
        # Extract the user's most recent message from the history
        last_user_message = next((item['parts'][0] for item in reversed(chat_history) if item['role'] == 'user'), "Hello")

        # Start a new chat session with the full history
        chat = model.start_chat(history=chat_history[:-1]) # History excluding the last message
        
        response = chat.send_message(last_user_message)
        return response.text
    except Exception as e:
        print(f"An error occurred in get_llm_response: {e}")
        raise

