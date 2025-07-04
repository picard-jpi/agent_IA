"""
Exemple : Révision de code complète avec plusieurs agents
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents import DevTeamAgents, CodeReviewWorkflow
from src.config import LLM_CONFIG


def code_review_example():
    """Exemple de révision de code avec workflow complet"""
    
    print("🔍 Exemple : Révision de Code Collaborative")
    print("=" * 60)
    
    # Vérifier la configuration
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Veuillez configurer OPENAI_API_KEY dans votre fichier .env")
        return
    
    # Initialiser l'équipe et le workflow
    team = DevTeamAgents(LLM_CONFIG)
    workflow = CodeReviewWorkflow(team)
    
    # Demande de développement
    code_request = """
Je veux créer une classe Python pour gérer un cache LRU (Least Recently Used).

Exigences :
- Capacité maximale configurable
- Méthodes get() et put()
- Éviction automatique des éléments les moins récemment utilisés
- Complexité O(1) pour get et put
- Thread-safe
- Documentation complète
- Tests unitaires

Pouvez-vous développer cette solution et la réviser ?
"""
    
    print("📋 Demande de développement :")
    print(code_request)
    print("\n🚀 Lancement du workflow de révision...")
    print("-" * 60)
    
    # Lancer le workflow
    workflow.start_code_review(code_request)


if __name__ == "__main__":
    code_review_example()