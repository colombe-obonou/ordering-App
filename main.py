from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import ChatRequest, ChatResponse, OrderDetails
from openai_service import generate_chat_response
import uvicorn
from typing import List, Dict

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        # Convertir les messages au format attendu par OpenAI
        messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]
        
        # Obtenir la réponse du chatbot
        response = generate_chat_response(messages)
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)