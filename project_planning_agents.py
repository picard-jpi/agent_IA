#!/usr/bin/env python3
"""
Cas d'usage AutoGen : Équipe virtuelle de planification de projet
================================================================

Ce script démontre l'utilisation d'AutoGen pour créer une équipe virtuelle
d'agents spécialisés qui collaborent pour planifier un projet de développement
d'application mobile.

Agents impliqués:
- Chef de projet (Project Manager)
- Développeur Backend (Backend Developer)
- Développeur Frontend/Mobile (Frontend Developer)
- Designer UX/UI (UX Designer)
- Testeur QA (QA Engineer)
- Critique/Reviewer (Project Reviewer)
"""

import os
from dotenv import load_dotenv
import autogen
from termcolor import colored

# Charger les variables d'environnement
load_dotenv()

def setup_config():
    """Configuration pour les modèles LLM"""
    config_list = [
        {
            "model": "gpt-4",
            "api_key": os.getenv("OPENAI_API_KEY"),
            "api_type": "openai"
        },
        {
            "model": "gpt-3.5-turbo",
            "api_key": os.getenv("OPENAI_API_KEY"),
            "api_type": "openai"
        }
    ]
    
    llm_config = {
        "config_list": config_list,
        "temperature": 0.7,
        "timeout": 120,
    }
    
    return llm_config

def create_agents(llm_config):
    """Création des agents spécialisés"""
    
    # Chef de projet - Coordonne l'équipe et définit les objectifs
    project_manager = autogen.AssistantAgent(
        name="ProjectManager",
        system_message="""Tu es un chef de projet expérimenté. Ton rôle est de:
        - Définir la vision et les objectifs du projet
        - Coordonner les différentes équipes
        - Établir les priorités et les délais
        - S'assurer que le projet reste dans les temps et le budget
        - Faciliter la communication entre les équipes
        
        Tu dois être organisé, pragmatique et orienté résultats.""",
        llm_config=llm_config,
    )
    
    # Développeur Backend - Expertise technique côté serveur
    backend_developer = autogen.AssistantAgent(
        name="BackendDeveloper",
        system_message="""Tu es un développeur backend senior spécialisé en:
        - Architecture de systèmes distribués
        - APIs REST et GraphQL
        - Bases de données (SQL/NoSQL)
        - Sécurité et authentification
        - Performance et scalabilité
        
        Tu apportes une perspective technique réaliste sur la faisabilité et les défis.""",
        llm_config=llm_config,
    )
    
    # Développeur Frontend/Mobile - Expertise interface utilisateur
    frontend_developer = autogen.AssistantAgent(
        name="FrontendDeveloper",
        system_message="""Tu es un développeur frontend/mobile expert en:
        - Développement d'applications mobiles (React Native, Flutter)
        - Interfaces utilisateur modernes et responsives
        - Intégration d'APIs
        - Performance côté client
        - Accessibilité et UX
        
        Tu te concentres sur l'expérience utilisateur et la qualité du code frontend.""",
        llm_config=llm_config,
    )
    
    # Designer UX/UI - Expertise expérience utilisateur
    ux_designer = autogen.AssistantAgent(
        name="UXDesigner",
        system_message="""Tu es un designer UX/UI expérimenté spécialisé en:
        - Recherche utilisateur et personas
        - Wireframes et prototypes
        - Design d'interfaces mobiles
        - Tests d'utilisabilité
        - Design thinking et méthodologie centrée utilisateur
        
        Tu places l'utilisateur final au centre de tes recommandations.""",
        llm_config=llm_config,
    )
    
    # Testeur QA - Expertise qualité et tests
    qa_engineer = autogen.AssistantAgent(
        name="QAEngineer",
        system_message="""Tu es un ingénieur QA expert en:
        - Stratégies de test (unitaires, intégration, e2e)
        - Tests automatisés et manuels
        - Tests de performance et sécurité
        - Outils de CI/CD
        - Assurance qualité processus
        
        Tu anticipes les problèmes et proposes des solutions de test robustes.""",
        llm_config=llm_config,
    )
    
    # Critique/Reviewer - Évalue et challenge les propositions
    project_reviewer = autogen.AssistantAgent(
        name="ProjectReviewer",
        system_message="""Tu es un consultant senior qui évalue les projets. Ton rôle est de:
        - Analyser la faisabilité globale du projet
        - Identifier les risques et les points d'amélioration
        - Challenger les assumptions de l'équipe
        - Proposer des alternatives ou optimisations
        - Donner une perspective externe et objective
        
        Tu es critique constructif et orienté amélioration continue.""",
        llm_config=llm_config,
    )
    
    # Utilisateur proxy pour initier les conversations
    user_proxy = autogen.UserProxyAgent(
        name="ProductOwner",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=0,
        code_execution_config={"use_docker": False},
        system_message="Tu représentes le client/product owner qui initie le projet."
    )
    
    return {
        "project_manager": project_manager,
        "backend_developer": backend_developer,
        "frontend_developer": frontend_developer,
        "ux_designer": ux_designer,
        "qa_engineer": qa_engineer,
        "project_reviewer": project_reviewer,
        "user_proxy": user_proxy
    }

def setup_group_chat(agents):
    """Configuration du chat de groupe avec tous les agents"""
    agents_list = [
        agents["user_proxy"],
        agents["project_manager"],
        agents["backend_developer"],
        agents["frontend_developer"],
        agents["ux_designer"],
        agents["qa_engineer"],
        agents["project_reviewer"]
    ]
    
    group_chat = autogen.GroupChat(
        agents=agents_list,
        messages=[],
        max_round=12,
        speaker_selection_method="round_robin"  # Rotation entre les agents
    )
    
    manager = autogen.GroupChatManager(
        groupchat=group_chat,
        llm_config=setup_config()
    )
    
    return manager

def main():
    """Fonction principale - Lance la simulation de planification"""
    print(colored("🚀 Démarrage de la session de planification de projet", "green", attrs=["bold"]))
    print(colored("=" * 60, "green"))
    
    # Configuration
    llm_config = setup_config()
    
    # Vérification de la clé API
    if not os.getenv("OPENAI_API_KEY"):
        print(colored("❌ Erreur: OPENAI_API_KEY non trouvée dans les variables d'environnement", "red"))
        print(colored("📝 Créez un fichier .env avec: OPENAI_API_KEY=votre_clé_api", "yellow"))
        return
    
    # Création des agents
    agents = create_agents(llm_config)
    
    # Configuration du chat de groupe
    manager = setup_group_chat(agents)
    
    # Définition du projet à planifier
    project_brief = """
    🎯 BRIEF PROJET: Application Mobile de Fitness Social
    
    Objectif: Développer une application mobile qui combine fitness tracking et social networking.
    
    Fonctionnalités principales souhaitées:
    - Suivi d'activités physiques (course, vélo, gym)
    - Défis entre amis et communauté
    - Plans d'entraînement personnalisés
    - Partage de progrès et achievements
    - Intégration avec appareils fitness (Apple Watch, Fitbit)
    - Système de récompenses et gamification
    
    Contraintes:
    - Lancement prévu dans 6 mois
    - Budget limité (startup)
    - Équipe de 4 développeurs
    - Cibler iOS et Android
    - Doit être conforme GDPR (données de santé)
    
    Question principale: Comment structurer ce projet pour maximiser nos chances de succès?
    """
    
    print(colored("📋 Brief du projet transmis aux agents...", "blue"))
    print(colored("-" * 40, "blue"))
    
    # Lancement de la conversation
    try:
        agents["user_proxy"].initiate_chat(
            manager,
            message=project_brief
        )
        
        print(colored("\n✅ Session de planification terminée avec succès!", "green", attrs=["bold"]))
        
    except Exception as e:
        print(colored(f"❌ Erreur durant la session: {e}", "red"))
        print(colored("💡 Vérifiez votre connexion internet et votre clé API OpenAI", "yellow"))

if __name__ == "__main__":
    main()