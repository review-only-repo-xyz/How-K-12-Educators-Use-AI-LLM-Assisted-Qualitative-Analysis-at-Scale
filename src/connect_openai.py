import openai
import os
from dotenv import load_dotenv

def connect_openai():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    try:
        openai.api_key = api_key
        return openai
    except Exception as e:
        raise Exception(f"Failed to initialize openai client: {str(e)}")
