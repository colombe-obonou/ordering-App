from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from models import OrderDetails

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Tu es un assistant de prise de commande pour une entreprise. Ton rôle est de:
1. Identifier ce que le client veut commander
2. Demander les informations spécifiques au produit (marque, modèle, taille, etc.)
3. Demander le nom, l'adresse et le contact du client
4. Résumer la commande sous forme JSON structuré et demander validation

Pour chaque commande, extraire les informations dans ce format:
{
    "article": "type de produit",
    "marque": "marque du produit",
    "modele": "modèle spécifique",
    "taille": "taille le cas échéant",
    "quantite": nombre,
    "nom_client": "nom complet",
    "adresse": "adresse de livraison",
    "contact": "email ou téléphone"
}

Si des informations manquent, pose des questions pour les obtenir.
Ne demande que la marque, le modèle, etc. si le produit est autre chose que la nourriture.
"""

def generate_chat_response(messages: list) -> dict:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
            temperature=0.7,
        )
        
        content = response.choices[0].message.content
        
        # Essayez d'extraire un JSON de la réponse
        try:
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            json_str = content[json_start:json_end]
            order_data = json.loads(json_str)
            
            return {
                "assistant_message": content,
                "order_detected": True,
                "extracted_data": order_data
            }
        except (ValueError, KeyError, json.JSONDecodeError):
            return {
                "assistant_message": content,
                "order_detected": False
            }
            
    except Exception as e:
        return {
            "assistant_message": f"Désolé, une erreur est survenue: {str(e)}",
            "order_detected": False
        }