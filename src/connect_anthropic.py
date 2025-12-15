from anthropic import Anthropic
from dotenv import load_dotenv
import os

def connect_anthropic():
    """
    Initialize and return an Anthropic client using API key from environment variables.
    
    Returns:
        Anthropic: Configured Anthropic client instance
        
    Raises:
        ValueError: If ANTHROPIC_API_KEY environment variable is not set
        Exception: If client initialization fails
    """
    load_dotenv()  # Load environment variables from .env
    
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
    
    try:
        client = Anthropic(api_key=api_key)
        return client
    except Exception as e:
        raise Exception(f"Failed to initialize Anthropic client: {str(e)}")