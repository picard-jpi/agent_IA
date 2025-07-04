"""
Script principal pour démontrer l'utilisation des agents AutoGen
"""

import os
import sys
from typing import Optional

# Ajouter le répertoire parent au path pour les imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents import DevTeamAgents, CodeReviewWorkflow, ProjectPlanningWorkflow
from src.config import LLM_CONFIG


def check_api_key():
    """Vérifier si la clé API est configurée"""
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Erreur : OPENAI_API_KEY n'est pas configurée")
        print("📝 Veuillez copier .env.example vers .env et configurer votre clé API")
        return False
    return True


def display_menu():
    """Afficher le menu principal"""
    print("\n" + "="*60)
    print("🤖 SYSTÈME D'AGENTS IA AVEC AUTOGEN")
    print("="*60)
    print("1. 💻 Révision de code collaborative")
    print("2. 📋 Planification de projet")
    print("3. 💬 Discussion libre avec l'équipe")
    print("4. ℹ️  Informations sur les agents")
    print("5. 🚪 Quitter")
    print("="*60)


def code_review_demo():
    """Démonstration de révision de code"""
    print("\n🔍 Mode Révision de Code")
    print("-" * 40)
    
    # Créer l'équipe d'agents
    team = DevTeamAgents(LLM_CONFIG)
    workflow = CodeReviewWorkflow(team)
    
    print("Décrivez le code que vous souhaitez développer/réviser :")
    print("(Exemple: 'Créer une fonction pour calculer la factorielle avec gestion d'erreurs')")
    
    code_request = input("\n📝 Votre demande : ").strip()
    
    if code_request:
        print("\n🚀 Lancement de la révision de code...")
        workflow.start_code_review(code_request)
    else:
        print("❌ Aucune demande fournie")


def project_planning_demo():
    """Démonstration de planification de projet"""
    print("\n📋 Mode Planification de Projet")
    print("-" * 40)
    
    team = DevTeamAgents(LLM_CONFIG)
    workflow = ProjectPlanningWorkflow(team)
    
    print("Décrivez votre projet :")
    print("(Exemple: 'Application web de gestion de tâches avec authentification utilisateur')")
    
    project_description = input("\n📝 Description du projet : ").strip()
    
    if project_description:
        print("\n🚀 Lancement de la planification...")
        workflow.start_project_planning(project_description)
    else:
        print("❌ Aucune description fournie")


def free_discussion():
    """Discussion libre avec l'équipe"""
    print("\n💬 Mode Discussion Libre")
    print("-" * 40)
    
    team = DevTeamAgents(LLM_CONFIG)
    
    # Permettre à l'utilisateur de choisir les agents
    print("Agents disponibles :")
    agents_list = ["developer", "reviewer", "tester", "project_manager"]
    for i, agent in enumerate(agents_list, 1):
        print(f"  {i}. {agent}")
    
    print("\nEntrez les numéros des agents que vous voulez inclure (ex: 1,2,4) :")
    selection = input("📝 Sélection : ").strip()
    
    try:
        selected_indices = [int(x.strip()) - 1 for x in selection.split(",")]
        selected_agents = [agents_list[i] for i in selected_indices if 0 <= i < len(agents_list)]
        
        if not selected_agents:
            selected_agents = agents_list
            
        print(f"\n👥 Agents sélectionnés : {', '.join(selected_agents)}")
        
        # Créer le groupe de discussion
        group_chat = team.create_group_chat(selected_agents)
        manager = team.create_group_chat_manager(group_chat)
        
        print("\nEntrez votre message pour l'équipe :")
        message = input("📝 Message : ").strip()
        
        if message:
            print("\n🚀 Début de la discussion...")
            team.user_proxy.initiate_chat(manager, message=message)
        else:
            print("❌ Aucun message fourni")
            
    except ValueError:
        print("❌ Sélection invalide, utilisation de tous les agents")
        group_chat = team.create_group_chat()
        manager = team.create_group_chat_manager(group_chat)
        
        message = input("\n📝 Votre message : ").strip()
        if message:
            team.user_proxy.initiate_chat(manager, message=message)


def show_agents_info():
    """Afficher les informations sur les agents"""
    print("\n👥 INFORMATIONS SUR LES AGENTS")
    print("="*60)
    
    agents_info = {
        "Développeur Senior": "Écrit du code propre et efficace, propose des solutions techniques optimales",
        "Réviseur de Code": "Analyse la qualité du code, identifie les bugs et suggère des améliorations",
        "Ingénieur Test": "Crée des tests unitaires et d'intégration, assure la couverture de code",
        "Chef de Projet": "Coordonne les activités, priorise les tâches et gère la qualité finale"
    }
    
    for agent, description in agents_info.items():
        print(f"\n🤖 {agent}")
        print(f"   {description}")
    
    print("\n" + "="*60)


def main():
    """Fonction principale"""
    print("🚀 Initialisation du système d'agents AutoGen...")
    
    # Vérifier la configuration
    if not check_api_key():
        return
    
    print("✅ Configuration validée")
    
    while True:
        display_menu()
        
        try:
            choice = input("\n👉 Votre choix (1-5) : ").strip()
            
            if choice == "1":
                code_review_demo()
            elif choice == "2":
                project_planning_demo()
            elif choice == "3":
                free_discussion()
            elif choice == "4":
                show_agents_info()
            elif choice == "5":
                print("\n👋 Au revoir !")
                break
            else:
                print("❌ Choix invalide, veuillez sélectionner 1-5")
                
        except KeyboardInterrupt:
            print("\n\n👋 Arrêt du programme")
            break
        except Exception as e:
            print(f"\n❌ Erreur : {e}")


if __name__ == "__main__":
    main()