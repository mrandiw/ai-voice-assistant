![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![PythonAnywhere](https://img.shields.io/badge/pythonanywhere-%232F9FD7.svg?style=for-the-badge&logo=pythonanywhere&logoColor=151515)
![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)

# AI Voice Assistant

A sophisticated voice-based AI assistant that operates entirely locally, integrating speech-to-text, text-to-speech, and large language model capabilities without relying on cloud services.

## Key Components

- **Speech Recognition**: Powered by OpenAI's Whisper model for accurate speech-to-text conversion
- **Voice Synthesis**: Implements Coqui TTS for natural-sounding text-to-speech responses
- **Language Processing**: Connects with Ollama to run large language models locally
- **User Interface**: Features an intuitive Gradio-based interface

## Architecture
![AI Voice Assistant](https://github.com/user-attachments/assets/9caf2d87-671e-482f-a953-0bb5b1a48000)


## System Requirements

- Python 3.12 or newer
- 8GB RAM minimum (16GB recommended)
- Storage: 2GB for base models
- NVIDIA GPU recommended for optimal performance

## Installation

### 1. Environment Setup

Create and activate a Python virtual environment:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate

# Ubuntu
python -m venv venv
source venv/bin/activate
```

### 2. Dependencies Installation

```bash
# Core dependencies
pip install -U openai-whisper coqui-tts sounddevice soundfile gradio

# For NVIDIA GPU acceleration
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 
```

### 3. Ollama Setup

Ensure [Ollama](https://ollama.ai/) is installed on your system for local LLM functionality.

```bash
# Pull a recommended model
ollama pull gemma3:1b
```

## Usage

Launch the application:

```bash
python main.py
```

The Gradio interface will start locally and can be accessed via your web browser.

## Features

### Speech Processing
- **Offline Speech Recognition**: Transcribe voice input without internet connectivity
- **Natural Voice Output**: Generate human-like speech responses
- **Voice Customization**: Multiple voice options available through Coqui TTS models

### AI Capabilities
- **Contextual Understanding**: Maintains conversation history for coherent interactions
- **Local Processing**: All data remains on your device for enhanced privacy
- **Extensible Architecture**: Easily integrate additional models or functionality

## Video Example
https://github.com/user-attachments/assets/21be38bb-11a5-4cc1-a6ed-d65b9b4db176



## Troubleshooting

For common issues, see our [troubleshooting guide](./docs/troubleshooting.md).

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
