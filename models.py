from pydantic import BaseModel
from typing import List, Dict, Optional

class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

class OrderDetails(BaseModel):
    article: str
    marque: Optional[str] = None
    modele: Optional[str] = None
    taille: Optional[str] = None
    quantite: Optional[int] = 1
    nom_client: Optional[str] = None
    adresse: Optional[str] = None
    contact: Optional[str] = None

class ChatResponse(BaseModel):
    assistant_message: str
    order_detected: bool
    extracted_data: Optional[OrderDetails] = None
    