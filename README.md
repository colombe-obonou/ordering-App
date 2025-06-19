

```mermaid
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


