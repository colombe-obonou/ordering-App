import streamlit as st
import requests
import json
from datetime import datetime

API_URL = "http://localhost:8000/chat"

def main():
    st.title("Rapid Commande")
    
    # Initialiser les sessions state
    if "chat_sessions" not in st.session_state:
        st.session_state.chat_sessions = {}
        st.session_state.current_session_id = None
        st.session_state.messages = []
    
    # Sidebar pour l'historique
    with st.sidebar:
        st.header("Historique des messages")
        
        # Boutons de gestion
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ New chat"):
                # Sauvegarder la session actuelle si elle existe
                if st.session_state.current_session_id is not None and st.session_state.messages:
                    st.session_state.chat_sessions[st.session_state.current_session_id]["messages"] = st.session_state.messages
                
                # Créer une nouvelle session
                new_session_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.session_state.current_session_id = new_session_id
                st.session_state.chat_sessions[new_session_id] = {
                    "created_at": new_session_id,
                    "messages": []
                }
                st.session_state.messages = []
                st.rerun()
        
        with col2:
            if st.button("♻️ Réinitialiser"):
                st.session_state.chat_sessions = {}
                st.session_state.current_session_id = None
                st.session_state.messages = []
                st.rerun()
        
        st.divider()
        
        # Liste des sessions
        if st.session_state.chat_sessions:
            for session_id, session_data in sorted(
                st.session_state.chat_sessions.items(), 
                key=lambda x: x[0], 
                reverse=True
            ):
                # Afficher un bouton pour chaque session
                if st.button(
                    f"🗨️ {session_id}", 
                    key=f"btn_{session_id}",
                    use_container_width=True
                ):
                    st.session_state.current_session_id = session_id
                    st.session_state.messages = session_data["messages"]
                    st.rerun()
        else:
            st.info("Aucune discussion")
    
    # Zone principale de chat
    # Afficher l'historique des messages de la session courante
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input utilisateur
    if prompt := st.chat_input("Ecrire votre message ici..."):
        # Ajouter le message de l'utilisateur à l'historique
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Envoyer l'historique à l'API
        try:
            response = requests.post(
                API_URL,
                json={"messages": st.session_state.messages},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                assistant_message = data["assistant_message"]
                
                # Afficher la réponse de l'assistant
                with st.chat_message("assistant"):
                    st.markdown(assistant_message)
                
                # Ajouter à l'historique
                st.session_state.messages.append({"role": "assistant", "content": assistant_message})
                
                # Si une commande est détectée, afficher le JSON
                if data.get("order_detected", False):
                    st.json(data["extracted_data"])
            else:
                st.error(f"Erreur API: {response.text}")
                
        except Exception as e:
            st.error(f"Erreur de connexion: {str(e)}")

if __name__ == "__main__":
    main()