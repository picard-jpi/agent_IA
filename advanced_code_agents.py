#!/usr/bin/env python3
"""
Exemple Avancé AutoGen : Agents avec Exécution de Code
======================================================

Cet exemple montre des agents capables d'exécuter du code Python
pour résoudre des problèmes d'analyse de données en temps réel.

Agents:
- Data Scientist: Analyse et modélisation
- Code Executor: Exécution sécurisée du code  
- Data Validator: Validation des résultats
"""

import os
from dotenv import load_dotenv
import autogen
from termcolor import colored

# Charger les variables d'environnement
load_dotenv()

def setup_code_config():
    """Configuration pour les agents avec exécution de code"""
    config_list = [
        {
            "model": "gpt-4",
            "api_key": os.getenv("OPENAI_API_KEY"),
        }
    ]
    
    llm_config = {
        "config_list": config_list,
        "temperature": 0.1,  # Plus conservateur pour le code
    }
    
    return llm_config

def create_data_science_team():
    """Création d'une équipe de data science avec exécution de code"""
    
    llm_config = setup_code_config()
    
    # Data Scientist - Écrit le code d'analyse
    data_scientist = autogen.AssistantAgent(
        name="DataScientist",
        system_message="""Tu es un data scientist expert. Tu écris du code Python pour:
        - Analyser des datasets
        - Créer des visualisations avec matplotlib/seaborn
        - Calculer des statistiques descriptives  
        - Développer des modèles prédictifs simples
        - Interpréter les résultats
        
        Utilise pandas, numpy, matplotlib, seaborn pour tes analyses.
        Toujours commenter ton code et expliquer tes choix méthodologiques.
        
        Format de réponse souhaité:
        1. Explication de l'approche
        2. Code Python avec commentaires
        3. Interprétation des résultats""",
        llm_config=llm_config,
    )
    
    # Exécuteur de code - Peut exécuter le code Python
    code_executor = autogen.UserProxyAgent(
        name="CodeExecutor",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=3,
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config={
            "work_dir": "data_analysis_workspace",
            "use_docker": False,  # Set to True for more security in production
        },
        system_message="""Tu exécutes le code Python fourni par le Data Scientist.
        Tu rapportes fidèlement les résultats d'exécution, erreurs, et outputs.
        Tu peux aussi suggérer des corrections si le code a des erreurs."""
    )
    
    # Validateur de données - Vérifie la qualité des analyses
    data_validator = autogen.AssistantAgent(
        name="DataValidator",
        system_message="""Tu es un expert en validation de données et analyses.
        Tu examines:
        - La qualité méthodologique des analyses
        - La justesse des interprétations statistiques
        - La robustesse des conclusions
        - Les biais potentiels dans les données ou méthodes
        
        Tu proposes des améliorations constructives et identifies les limites.""",
        llm_config=llm_config,
    )
    
    return data_scientist, code_executor, data_validator

def run_data_analysis_session():
    """Lance une session d'analyse de données collaborative"""
    
    print(colored("🔬 Session d'Analyse de Données Collaborative", "green", attrs=["bold"]))
    print(colored("=" * 55, "green"))
    
    if not os.getenv("OPENAI_API_KEY"):
        print(colored("❌ OPENAI_API_KEY requise", "red"))
        return
    
    # Création de l'équipe
    scientist, executor, validator = create_data_science_team()
    
    # Problème d'analyse à résoudre
    analysis_task = """
    🎯 MISSION D'ANALYSE:
    
    Nous avons des données de ventes simulées à analyser. 
    
    TÂCHES:
    1. Générer un dataset de ventes simulé (500 lignes)
       - Colonnes: date, produit, prix, quantité, région, vendeur
       - Période: 12 derniers mois
       - 5 produits différents, 3 régions, 10 vendeurs
    
    2. Effectuer une analyse exploratoire:
       - Statistiques descriptives
       - Tendances temporelles
       - Performance par région/vendeur/produit
       - Visualisations pertinentes
    
    3. Identifier les insights business clés
    
    4. Détecter les anomalies ou patterns intéressants
    
    Commencez par créer le dataset puis analysez-le étape par étape.
    """
    
    print(colored("📊 Lancement de l'analyse...", "blue"))
    
    try:
        # Le Data Scientist initie l'analyse
        executor.initiate_chat(
            scientist,
            message=analysis_task,
            max_turns=8
        )
        
        print(colored("\n" + "="*50, "cyan"))
        print(colored("🔍 Phase de Validation", "magenta"))
        
        # Le validateur examine les résultats
        scientist.initiate_chat(
            validator,
            message="""Maintenant que nous avons effectué l'analyse, 
            peux-tu examiner la méthodologie utilisée et les résultats obtenus? 
            Que penses-tu de la qualité de cette analyse? Y a-t-il des améliorations à apporter?""",
            max_turns=4
        )
        
        print(colored("\n✅ Session d'analyse terminée!", "green", attrs=["bold"]))
        
    except Exception as e:
        print(colored(f"❌ Erreur durant l'analyse: {e}", "red"))

def create_sample_notebook():
    """Crée un notebook Jupyter d'exemple pour l'analyse"""
    
    notebook_content = '''
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 📊 Analyse de Données Collaborative AutoGen\\n",
    "\\n",
    "Ce notebook complète les exemples AutoGen en montrant comment\\n",
    "intégrer les agents dans un workflow Jupyter."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Import des librairies\\n",
    "import pandas as pd\\n",
    "import numpy as np\\n",
    "import matplotlib.pyplot as plt\\n",
    "import seaborn as sns\\n",
    "from datetime import datetime, timedelta\\n",
    "\\n",
    "# Configuration des graphiques\\n",
    "plt.style.use('seaborn-v0_8')\\n",
    "sns.set_palette('husl')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 🎯 Intégration avec AutoGen\\n",
    "\\n",
    "Les agents AutoGen peuvent générer du code à exécuter dans ce notebook:\\n",
    "\\n",
    "```python\\n",
    "# Code généré par l'agent DataScientist\\n",
    "# puis exécuté par l'agent CodeExecutor\\n",
    "# puis validé par l'agent DataValidator\\n",
    "```"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
'''
    
    with open("data_analysis_example.ipynb", "w", encoding="utf-8") as f:
        f.write(notebook_content)
    
    print(colored("📓 Notebook Jupyter créé: data_analysis_example.ipynb", "cyan"))

def main():
    """Fonction principale pour l'exemple avancé"""
    
    print(colored("🧬 AUTOGEN AVANCÉ - AGENTS AVEC CODE", "yellow", attrs=["bold"]))
    print(colored("=" * 40, "yellow"))
    print("1. 🔬 Session d'analyse collaborative")
    print("2. 📓 Créer notebook Jupyter d'exemple")
    print("3. 🏠 Retour au menu principal")
    print()
    
    choice = input(colored("Votre choix (1-3): ", "cyan"))
    
    if choice == "1":
        run_data_analysis_session()
    elif choice == "2":
        create_sample_notebook()
    elif choice == "3":
        from simple_agents_example import main as simple_main
        simple_main()
    else:
        print(colored("Choix invalide!", "red"))

if __name__ == "__main__":
    main()