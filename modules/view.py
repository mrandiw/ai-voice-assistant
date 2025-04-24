import gradio as gr
from modules.utils import fix_encoding

class GradioInterface:
    def __init__(self, speech_processor, text_processor):
        """
        Initialize the Gradio interface
        
        Args:
            speech_processor: Function to process speech input
            text_processor: Function to process text input
        """
        self.speech_processor = speech_processor
        self.text_processor = text_processor
        
    def create_interface(self):
        """Create and return the Gradio interface"""
        with gr.Blocks(title="Voice Assistant") as app:
            gr.Markdown("# Voice Assistant")
            
            with gr.Tab("Voice to Text"):
                with gr.Row():
                    with gr.Column():
                        audio_input = gr.Audio(type="filepath", label="Upload Audio")
                        voice_submit_btn = gr.Button("Process Voice Input")
                    
                    with gr.Column():
                        transcription_output = gr.Textbox(label="Transcription")
                        response_output = gr.Textbox(label="Assistant Response")
                        audio_output = gr.Audio(label="Assistant Speech Response")
                
                voice_submit_btn.click(
                    fn=self.speech_processor, 
                    inputs=[audio_input], 
                    outputs=[transcription_output, response_output, audio_output]
                )
            
            with gr.Tab("Text Input"):
                with gr.Row():
                    with gr.Column():
                        text_input = gr.Textbox(lines=3, label="Type your message")
                        text_submit_btn = gr.Button("Send")
                    
                    with gr.Column():
                        text_response_output = gr.Textbox(label="Assistant Response")
                        text_audio_output = gr.Audio(label="Speech Output")
                
                text_submit_btn.click(
                    fn=self.text_processor,
                    inputs=[text_input],
                    outputs=[text_response_output, text_audio_output]
                )
            
            gr.Markdown("""
            ## Instructions
            1. Use the "Voice to Text" tab to speak to the assistant
            2. Use the "Text Input" tab to type your query
            3. The system will transcribe your voice or process your text and generate a response
            4. The response will be converted to speech automatically
            """)
        
        return app