import whisper
import torch

class SpeechToText:
    def __init__(self):
        """Initialize the Speech-to-Text model"""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"STT using device: {self.device}")
        
        # Load speech-to-text model
        print("Loading STT model...")
        self.model = whisper.load_model("base")
    
    def transcribe(self, audio_file):
        """
        Transcribe audio file to text
        
        Args:
            audio_file (str): Path to audio file
            
        Returns:
            str: Transcribed text
        """
        if audio_file is None:
            return ""
            
        try:
            result = self.model.transcribe(audio_file)
            transcription = result["text"]
            return transcription
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return ""