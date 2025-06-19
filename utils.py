import re
import json

def extract_json_from_text(text: str) -> dict:
    """Essaye d'extraire un JSON du texte de réponse"""
    try:
        # Cherche le premier { et dernier } dans le texte
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            return json.loads(json_str)
        return None
    except (ValueError, json.JSONDecodeError):
        return None

def validate_order_data(data: dict) -> bool:
    """Valide que les données de commande ont les champs requis"""
    required_fields = ["article", "nom_client", "adresse", "contact"]
    return all(field in data for field in required_fields)