#!/usr/bin/env python3
"""
Exemple simple AutoGen : Résolution collaborative de problèmes
==============================================================

Cet exemple montre une interaction basique entre deux agents:
- Un expert en analyse de données
- Un expert en visualisation de données

Ils collaborent pour analyser un dataset et créer des recommandations.
"""

import os
from dotenv import load_dotenv
import autogen
from termcolor import colored

# Charger les variables d'environnement
load_dotenv()

def setup_simple_config():
    """Configuration simplifiée pour les modèles LLM"""
    config_list = [
        {
            "model": "gpt-3.5-turbo",
            "api_key": os.getenv("OPENAI_API_KEY"),
        }
    ]
    
    llm_config = {
        "config_list": config_list,
        "temperature": 0.7,
    }
    
    return llm_config

def create_analysis_team():
    """Création d'une équipe d'analyse simple"""
    
    llm_config = setup_simple_config()
    
    # Expert en analyse de données
    data_analyst = autogen.AssistantAgent(
        name="DataAnalyst",
        system_message="""Tu es un analyste de données expert. Ton rôle est de:
        - Analyser les données et identifier les tendances
        - Proposer des méthodes d'analyse appropriées
        - Interpréter les résultats statistiques
        - Identifier les insights business importants
        
        Tu communiques de manière claire et précise.""",
        llm_config=llm_config,
    )
    
    # Expert en visualisation
    data_visualizer = autogen.AssistantAgent(
        name="DataVisualizer",
        system_message="""Tu es un expert en visualisation de données. Ton rôle est de:
        - Recommander les meilleurs types de graphiques
        - Créer des dashboards efficaces
        - Optimiser la présentation des données
        - Assurer la clarté et l'impact visuel
        
        Tu te concentres sur l'storytelling avec les données.""",
        llm_config=llm_config,
    )
    
    # Utilisateur qui initie l'analyse
    user_proxy = autogen.UserProxyAgent(
        name="BusinessManager",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=0,
        code_execution_config={"use_docker": False},
    )
    
    return data_analyst, data_visualizer, user_proxy

def run_simple_analysis():
    """Lance une analyse collaborative simple"""
    
    print(colored("🔍 Lancement de l'analyse collaborative", "cyan", attrs=["bold"]))
    print(colored("=" * 50, "cyan"))
    
    # Vérification de la clé API
    if not os.getenv("OPENAI_API_KEY"):
        print(colored("❌ OPENAI_API_KEY manquante dans .env", "red"))
        return
    
    # Création de l'équipe
    analyst, visualizer, user = create_analysis_team()
    
    # Problème à résoudre
    business_problem = """
    📊 CONTEXTE BUSINESS:
    
    Notre e-commerce a ces données de vente du dernier trimestre:
    - Revenus mensuels: Janvier 50K€, Février 45K€, Mars 62K€
    - Top 3 catégories: Électronique (35%), Vêtements (28%), Maison (18%)
    - Taux de conversion: 2.1% (objectif: 3%)
    - Panier moyen: 85€ (en baisse de 8% vs trimestre précédent)
    - 60% trafic mobile, 40% desktop
    - Retours produits: 12% (en hausse)
    
    QUESTIONS:
    1. Que révèlent ces données sur la performance?
    2. Quelles visualisations créer pour le board?
    3. Quelles actions recommander?
    
    Merci de collaborer pour une analyse complète.
    """
    
    print(colored("📋 Problème soumis aux experts...", "blue"))
    
    try:
        # L'analyste commence l'analyse
        user.initiate_chat(
            analyst,
            message=business_problem,
            max_turns=6
        )
        
        print(colored("\n" + "="*50, "cyan"))
        print(colored("🎨 Phase visualisation - Collaboration avec le visualiseur", "magenta"))
        
        # Le visualiseur rejoint pour la partie présentation
        analyst.initiate_chat(
            visualizer,
            message="""Maintenant que j'ai analysé les données business, 
            collaborons pour créer les meilleures visualisations pour présenter 
            ces insights au comité de direction. Quels graphiques recommandes-tu?""",
            max_turns=4
        )
        
        print(colored("\n✅ Analyse collaborative terminée!", "green", attrs=["bold"]))
        
    except Exception as e:
        print(colored(f"❌ Erreur: {e}", "red"))

def main():
    """Fonction principale avec menu de choix"""
    
    print(colored("🤖 EXEMPLES AUTOGEN", "yellow", attrs=["bold"]))
    print(colored("=" * 40, "yellow"))
    print("1. 🏢 Équipe complète de planification projet")
    print("2. 🔍 Analyse collaborative simple (2 agents)")
    print("3. 🧬 Agents avancés avec exécution de code")
    print()
    
    choice = input(colored("Choisir un exemple (1-3): ", "cyan"))
    
    if choice == "1":
        # Import et lancement de l'exemple complexe
        from project_planning_agents import main as complex_main
        complex_main()
    elif choice == "2":
        run_simple_analysis()
    elif choice == "3":
        # Import et lancement de l'exemple avancé
        from advanced_code_agents import main as advanced_main
        advanced_main()
    else:
        print(colored("Choix invalide!", "red"))

if __name__ == "__main__":
    main()