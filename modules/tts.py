import os
import uuid
from TTS.api import TTS

class TextToSpeech:
    def __init__(self):
        """Initialize the Text-to-Speech model"""
        print("Loading TTS model...")
        try:
            self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)
            self.available = True
        except Exception as e:
            print(f"Failed to load the default TTS model: {e}")
            self.tts = None
            self.available = False
        
        # Ensure temp directory exists
        self.temp_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "temp")
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

    def generate_speech(self, text):
        """
        Generate speech from text
        
        Args:
            text (str): Text to convert to speech
            
        Returns:
            str: Path to generated audio file or None if failed
        """
        if not text or not text.strip() or not self.available:
            return None
            
        try:
            # Create a unique filename in the temp directory
            filename = f"tts_{uuid.uuid4().hex}.wav"
            file_path = os.path.join(self.temp_dir, filename)
            
            # Generate speech and save to the file
            self.tts.tts_to_file(text=text, file_path=file_path)
            
            return file_path
        except Exception as e:
            print(f"Error generating speech: {e}")
            return None