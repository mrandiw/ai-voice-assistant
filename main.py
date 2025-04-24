import torch
import warnings
import numpy as np
import sounddevice as sd
from modules.stt import SpeechToText
from modules.tts import TextToSpeech
from modules.llm import LLMHandler
from modules.view import GradioInterface
from modules.utils import fix_encoding, cleanup_temp_files

# Suppress warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

class VoiceAssistant:
    def __init__(self):
        """Initialize the voice assistant with all components"""
        # Initialize components
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.llm = LLMHandler()
        
        # Define processor functions for the UI
        self.ui = GradioInterface(
            speech_processor=self.process_voice,
            text_processor=self.process_text
        )
    
    def process_voice(self, audio_file):
        """Process voice input from user"""
        if audio_file is None:
            return "No audio detected", "No audio detected", None
        
        try:
            # Transcribe audio
            transcription = self.stt.transcribe(audio_file)
            
            # Fix encoding in transcription
            fixed_transcription = fix_encoding(transcription)
            
            # Get response from LLM
            response = self.llm.query(fixed_transcription)
            
            # Generate speech from response
            speech_file = self.tts.generate_speech(response)
            
            return fixed_transcription, response, speech_file
                
        except Exception as e:
            error_message = f"Error processing voice: {str(e)}"
            return error_message, error_message, None
    
    def process_text(self, text_input):
        """Process text input from user"""
        if not text_input or not text_input.strip():
            return "No text input provided", None
        
        try:
            # Fix encoding in input
            fixed_input = fix_encoding(text_input)
            
            # Get response from LLM
            response = self.llm.query(fixed_input)
            
            # Generate speech from response
            speech_file = self.tts.generate_speech(response)
            
            return response, speech_file
                
        except Exception as e:
            error_message = f"Error processing text: {str(e)}"
            return error_message, None

    def run(self):
        """Run the voice assistant application"""
        app = self.ui.create_interface()
        print("Starting Gradio server...")
        try:
            app.launch()  # Set share=False if you don't want a public link
        finally:
            # Clean up temp files when the server shuts down
            cleanup_temp_files()

def main():
    assistant = VoiceAssistant()
    assistant.run()

if __name__ == "__main__":
    main()