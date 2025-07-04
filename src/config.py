"""
Configuration pour les agents AutoGen
"""

import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration des modèles LLM
LLM_CONFIG = {
    "model": "gpt-4",
    "api_key": os.getenv("OPENAI_API_KEY"),
    "temperature": 0.7,
    "max_tokens": 1000,
}

# Configuration alternative pour Azure OpenAI (si disponible)
AZURE_LLM_CONFIG = {
    "model": "gpt-4",
    "api_type": "azure",
    "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
    "api_base": os.getenv("AZURE_OPENAI_ENDPOINT"),
    "api_version": os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
    "temperature": 0.7,
    "max_tokens": 1000,
}

# Configuration des agents
AGENT_CONFIGS = {
    "developer": {
        "name": "Développeur_Senior",
        "system_message": """Vous êtes un développeur senior expérimenté. Votre rôle est de :
        - Écrire du code propre, efficace et bien documenté
        - Proposer des solutions techniques optimales
        - Suivre les meilleures pratiques de développement
        - Expliquer vos choix techniques
        
        Répondez toujours en français et structurez vos réponses clairement.""",
        "llm_config": LLM_CONFIG
    },
    
    "reviewer": {
        "name": "Réviseur_Code",
        "system_message": """Vous êtes un expert en révision de code. Votre rôle est de :
        - Analyser la qualité du code proposé
        - Identifier les bugs potentiels et problèmes de sécurité
        - Suggérer des améliorations en termes de performance et lisibilité
        - Vérifier le respect des conventions de code
        
        Soyez constructif dans vos critiques et proposez des solutions.""",
        "llm_config": LLM_CONFIG
    },
    
    "tester": {
        "name": "Ingénieur_Test",
        "system_message": """Vous êtes un ingénieur en tests logiciels. Votre rôle est de :
        - Créer des tests unitaires et d'intégration
        - Identifier les cas de test critiques
        - Proposer des stratégies de test
        - Assurer la couverture de code
        
        Focalisez-vous sur la création de tests robustes et maintenables.""",
        "llm_config": LLM_CONFIG
    },
    
    "project_manager": {
        "name": "Chef_Projet",
        "system_message": """Vous êtes un chef de projet technique. Votre rôle est de :
        - Coordonner les activités entre les différents agents
        - Prioriser les tâches et gérer les délais
        - Synthétiser les discussions et prendre des décisions
        - Assurer la qualité finale du livrable
        
        Gardez une vue d'ensemble du projet et guidez l'équipe vers les objectifs.""",
        "llm_config": LLM_CONFIG
    }
}

# Configuration de l'utilisateur
USER_PROXY_CONFIG = {
    "name": "Utilisateur",
    "human_input_mode": "ALWAYS",
    "max_consecutive_auto_reply": 3,
    "code_execution_config": {
        "work_dir": "coding",
        "use_docker": False,
    }
}