# Amol's AI Chatbot

A chatbot powered by Google Gemini API with two interfaces:
- **CLI Interface** (`chatbot.py`): Terminal-based chatbot
- **Web Interface** (`app.py`): Streamlit-based web application

## Features
- Interactive conversations with Google Gemini
- Conversation history maintained across interactions
- Clean and user-friendly interface

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

### CLI Version
```bash
python chatbot.py
```

### Web Version
```bash
streamlit run app.py
```

## Requirements
- Python 3.8+
- google-genai
- python-dotenv
- streamlit (for web version)
