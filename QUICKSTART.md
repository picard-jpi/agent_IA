# 🚀 Guide de Démarrage Rapide - AutoGen Agents

## ⚡ Installation Express (5 minutes)

### 1. Installation Automatique
```bash
# Cloner le projet (si applicable)
git clone <url-du-repo>
cd autogen-agents

# Installation automatique
python setup_environment.py
```

### 2. Configuration de la Clé API
```bash
# Éditer le fichier .env
nano .env

# Ajouter votre clé OpenAI
OPENAI_API_KEY=sk-votre-cle-ici
```

### 3. Test Rapide
```bash
# Méthode 1 : Script d'exemples
python run_examples.py

# Méthode 2 : Interface terminal
python src/main.py

# Méthode 3 : Interface web
streamlit run src/streamlit_app.py
```

## 🎯 Premier Usage

### Chat Simple avec un Agent
```python
from src.agents import DevTeamAgents
from src.config import LLM_CONFIG

# Créer l'équipe
team = DevTeamAgents(LLM_CONFIG)
developer = team.get_agent("developer")

# Poser une question
team.user_proxy.initiate_chat(
    developer,
    message="Créer une fonction de tri en Python"
)
```

### Révision de Code
```python
from src.agents import CodeReviewWorkflow

team = DevTeamAgents(LLM_CONFIG)
workflow = CodeReviewWorkflow(team)

workflow.start_code_review(
    "Je veux créer une API REST pour gérer des utilisateurs"
)
```

## 🛠️ Outils VSCode

### Tâches Disponibles
- `Ctrl+Shift+P` → "Tasks: Run Task"
- **Install Dependencies** : Installation automatique
- **Run Main Agent** : Lancer l'interface terminal
- **Run Streamlit App** : Interface web

### Débogage
- `F5` → Lancer le débogueur
- Configurations disponibles :
  - Python: Main Agent
  - Python: Simple Chat Example
  - Streamlit: Web App

## 🐛 Résolution Rapide

### Problème : Clé API
```bash
# Vérifier le fichier .env
cat .env

# Si vide, copier depuis l'exemple
cp .env.example .env
```

### Problème : Import AutoGen
```bash
# Réinstaller
pip install --upgrade autogen-agentchat
```

### Problème : Streamlit
```bash
# Réinstaller
pip install --upgrade streamlit
streamlit hello  # Test
```

## 📋 Cas d'Usage Populaires

### 1. Assistant de Développement
- **Utilisation** : Développement rapide de fonctions
- **Agents** : Développeur + Réviseur
- **Interface** : Terminal ou Web

### 2. Révision de Code
- **Utilisation** : Amélioration de code existant
- **Agents** : Développeur + Réviseur + Testeur
- **Interface** : Terminal recommandé

### 3. Planification de Projet
- **Utilisation** : Architecture et planification
- **Agents** : Chef de Projet + Développeur
- **Interface** : Web recommandé

## 🔧 Personnalisation Rapide

### Modifier un Agent
```python
# Dans src/config.py
AGENT_CONFIGS["developer"]["system_message"] = """
Nouveau comportement pour le développeur...
"""
```

### Ajouter un Agent
```python
# Dans src/agents.py
self.agents["data_scientist"] = autogen.AssistantAgent(
    name="Data_Scientist",
    system_message="Expert en données...",
    llm_config=self.llm_config
)
```

## 📞 Support Express

### Vérifications Automatiques
```bash
# Script de diagnostic
python -c "
import os
print('API Key:', '✅' if os.getenv('OPENAI_API_KEY') else '❌')

try:
    import autogen
    print('AutoGen:', '✅')
except:
    print('AutoGen:', '❌')

try:
    from src.config import LLM_CONFIG
    print('Config:', '✅')
except:
    print('Config:', '❌')
"
```

### Liens Utiles
- 📚 [Documentation AutoGen](https://github.com/microsoft/autogen)
- 🔧 [Configuration OpenAI](https://platform.openai.com/api-keys)
- 💬 [Support Streamlit](https://docs.streamlit.io/)

---

🎉 **Prêt à démarrer !** En moins de 5 minutes, vous avez une équipe d'agents IA opérationnelle.