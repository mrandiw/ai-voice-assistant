import subprocess
from modules.utils import fix_encoding

class LLMHandler:
    def __init__(self, model_name="gemma3:1b"):
        """Initialize the LLM handler with a specified model"""
        self.model_name = model_name
        print(f"LLM initializing with model: {model_name}")

    def query(self, prompt):
        """
        Send a query to the LLM and get a response
        
        Args:
            prompt (str): The user's prompt
            
        Returns:
            str: The LLM's response
        """
        # Create a system prompt for concise responses
        system_prompt = "Answer concisely and accurately in three sentences or less."
        
        # Combine system prompt with user prompt
        formatted_prompt = f"<s>{system_prompt}</s>\n<user>{prompt}</user>"
        
        try:
            result = subprocess.run(["ollama", "run", self.model_name, formatted_prompt], 
                                capture_output=True, text=True, timeout=30)
            # Sanitize the output from Ollama 
            raw_response = result.stdout.strip()
            print(f"Raw response from Ollama: {raw_response}")
            
            # Fix encoding issues in the Ollama response
            fixed_response = fix_encoding(raw_response)
            
            return fixed_response
        except subprocess.TimeoutExpired:
            return "Sorry, the model took too long to respond."
        except Exception as e:
            return f"Error querying Ollama: {str(e)}"