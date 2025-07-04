"""
Exemple simple : Chat avec un seul agent
"""

import os
import sys

# Ajouter le répertoire parent au path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents import DevTeamAgents
from src.config import LLM_CONFIG


def simple_developer_chat():
    """Exemple de chat simple avec le développeur senior"""
    
    print("🤖 Exemple : Chat avec le Développeur Senior")
    print("=" * 50)
    
    # Vérifier la clé API
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Veuillez configurer OPENAI_API_KEY dans votre fichier .env")
        return
    
    # Initialiser l'équipe
    team = DevTeamAgents(LLM_CONFIG)
    developer = team.get_agent("developer")
    user_proxy = team.user_proxy
    
    # Question simple
    question = """Peux-tu me créer une fonction Python pour valider une adresse email ?
La fonction doit :
- Utiliser des expressions régulières
- Retourner True/False
- Inclure une documentation
- Gérer les cas d'erreur"""
    
    print(f"📝 Question : {question}")
    print("\n🚀 Début de la conversation...")
    print("-" * 50)
    
    # Démarrer la conversation
    user_proxy.initiate_chat(
        developer,
        message=question,
        max_turns=3
    )


if __name__ == "__main__":
    simple_developer_chat()