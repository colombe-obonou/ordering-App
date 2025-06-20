# Order Management Chatbot

![Chatbot Demo](https://img.shields.io/badge/Demo-Streamlit-FF4B4B?logo=streamlit) 
![API](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi) 
![AI](https://img.shields.io/badge/Powered%20by-OpenAI-412991?logo=openai)

An intelligent chatbot solution for automated customer order processing through conversational API.

## Key Features

- **Universal order handling** - Supports any product type (electronics, food, etc.)
- **Smart data collection**:
  - Product specifications (brand, model, size)
  - Customer details (name, address, contact)
- **Structured output** - Automatically generates validated JSON orders
- **Streaming interface** - Real-time chat experience

## Tech Stack

graph LR
    A[Streamlit UI] --> B[FastAPI]
    B --> C[OpenAI Integration]
    C --> D[JSON Validation]

Installation:
git clone https://github.com/yourusername/chatbot-commande.git
cd chatbot-commande

pip install -r requirements.txt

echo "OPENAI_API_KEY=your_api_key_here" > .env

Usage:
python main.py
streamlit run streamlit_app.py
Access the chatbot at http://localhost:8501

Project structure:
chatbot-commande/
├── main.py               # FastAPI backend
├── openai_service.py     # OpenAI integration
├── model.py             # Data models
├── utils.py             # Helper functions
├── streamlit_app.py      # Chat interface
└── requirements.txt      # Dependencies


