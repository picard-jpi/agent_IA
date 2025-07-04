# 🤖 Système d'Agents IA avec AutoGen

Un use case complet d'agents IA collaboratifs utilisant AutoGen, optimisé pour VSCode avec interface web Streamlit.

## 📋 Table des Matières

- [🎯 Présentation](#-présentation)
- [✨ Fonctionnalités](#-fonctionnalités)
- [🛠️ Installation](#-installation)
- [⚙️ Configuration](#-configuration)
- [🧪 Test d'Installation](#-test-dinstallation)
- [🚀 Utilisation](#-utilisation)
- [👥 Agents Disponibles](#-agents-disponibles)
- [📁 Structure du Projet](#-structure-du-projet)
- [💡 Exemples](#-exemples)
- [🔧 Personnalisation](#-personnalisation)
- [🐛 Dépannage](#-dépannage)

## 🎯 Présentation

Ce projet démontre l'utilisation d'**AutoGen** pour créer une équipe d'agents IA spécialisés dans l'assistance au développement. Les agents collaborent pour :

- 💻 Développer du code de qualité
- 🔍 Réviser et améliorer le code existant  
- 🧪 Créer des tests appropriés
- 📋 Planifier des projets techniques

## ✨ Fonctionnalités

### 🎭 Agents Spécialisés
- **Développeur Senior** : Code propre et solutions techniques
- **Réviseur de Code** : Analyse qualité et améliorations
- **Ingénieur Test** : Tests unitaires et couverture
- **Chef de Projet** : Coordination et planification

### 🖥️ Interfaces Multiples
- **Terminal interactif** : Interface en ligne de commande
- **Interface web Streamlit** : UI moderne et intuitive
- **Notebooks Jupyter** : Démonstrations et expérimentations

### 🔄 Workflows Prêts à l'Emploi
- Révision de code collaborative
- Planification de projet
- Discussion libre en équipe

## 🛠️ Installation

### Prérequis
- Python 3.8+
- Clé API OpenAI
- VSCode (recommandé)

### Installation Rapide

```bash
# Installation automatique
python setup_environment.py
```

### Installation Manuelle

```bash
# Cloner le projet (si applicable)
git clone <url-du-repo>
cd autogen-agents

# Installer les dépendances
pip install -r requirements.txt
```

### Extensions VSCode Recommandées

Le projet inclut une configuration VSCode optimisée. Les extensions recommandées s'installent automatiquement :

- Python
- Jupyter
- Black Formatter
- Ruff (linting)

## ⚙️ Configuration

### 1. Variables d'Environnement

```bash
# Copier le fichier d'exemple
cp .env.example .env

# Éditer le fichier .env avec votre clé API
nano .env
```

### 2. Configuration .env

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Optionnel : Azure OpenAI
# AZURE_OPENAI_API_KEY=your_azure_key
# AZURE_OPENAI_ENDPOINT=your_azure_endpoint
# AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

### 3. Vérification de l'Installation

```bash
# Tester l'installation
python -c "import autogen; print('✅ AutoGen installé')"
```

## 🧪 Test d'Installation

Un script de test complet est fourni pour vérifier votre installation :

```bash
# Lancer le test d'installation
python test_installation.py
```

Ce script vérifie :
- ✅ Imports des modules nécessaires
- ✅ Structure du projet complète
- ✅ Configuration des variables d'environnement
- ✅ Création des agents
- ✅ Intégration VSCode

**Résultat attendu :** Tous les tests doivent passer pour une installation complète.

## 🚀 Utilisation

### 🖥️ Interface Terminal

```bash
# Lancer l'interface interactive
python src/main.py
```

Menu disponible :
1. 💻 Révision de code collaborative
2. 📋 Planification de projet  
3. 💬 Discussion libre avec l'équipe
4. ℹ️ Informations sur les agents
5. 🚪 Quitter

### 🌐 Interface Web Streamlit

```bash
# Lancer l'interface web
streamlit run src/streamlit_app.py
```

Accédez à `http://localhost:8501` pour utiliser l'interface web.

### 📓 Notebooks Jupyter

```bash
# Lancer Jupyter
jupyter notebook notebooks/
```

Ouvrez `demo_autogen.ipynb` pour une démonstration complète.

### ⚡ Tâches VSCode

Utilisez `Ctrl+Shift+P` puis "Tasks: Run Task" :
- **Install Dependencies** : Installer les dépendances
- **Run Main Agent** : Lancer l'interface terminal
- **Run Streamlit App** : Lancer l'interface web

### 🎯 Script d'Exemples

```bash
# Lancer le sélecteur d'exemples
python run_examples.py
```

## 👥 Agents Disponibles

### 🧑‍💻 Développeur Senior
- **Rôle** : Écriture de code propre et efficace
- **Spécialités** : Solutions techniques, bonnes pratiques
- **Utilisation** : Développement initial, architecture

### 🔍 Réviseur de Code  
- **Rôle** : Analyse et amélioration du code
- **Spécialités** : Qualité, sécurité, performance
- **Utilisation** : Code review, optimisation

### 🧪 Ingénieur Test
- **Rôle** : Tests et validation
- **Spécialités** : Tests unitaires, couverture, stratégies
- **Utilisation** : Création de tests, validation

### 📋 Chef de Projet
- **Rôle** : Coordination et planification
- **Spécialités** : Gestion, priorisation, synthèse
- **Utilisation** : Planification, coordination d'équipe

## 📁 Structure du Projet

```
autogen-agents/
├── .vscode/                    # Configuration VSCode
│   ├── tasks.json             # Tâches automatisées
│   ├── launch.json            # Configuration débogage
│   └── extensions.json        # Extensions recommandées
├── src/                       # Code source principal
│   ├── __init__.py           # Package Python
│   ├── config.py             # Configuration des agents
│   ├── agents.py             # Classes d'agents et workflows
│   ├── main.py               # Interface terminal
│   └── streamlit_app.py      # Interface web
├── examples/                  # Exemples d'utilisation
│   ├── simple_chat.py        # Chat simple
│   └── code_review_example.py # Révision complète
├── notebooks/                 # Notebooks Jupyter
│   └── demo_autogen.ipynb    # Démonstration complète
├── requirements.txt          # Dépendances Python
├── setup_environment.py     # Installation automatique
├── run_examples.py          # Script d'exemples
├── test_installation.py     # Test d'installation
├── .env.example             # Template variables d'environnement
├── .gitignore              # Fichiers à ignorer
├── QUICKSTART.md           # Guide démarrage rapide
└── README.md               # Documentation
```

## 💡 Exemples

### Chat Simple avec un Agent

```python
from src.agents import DevTeamAgents
from src.config import LLM_CONFIG

# Initialiser l'équipe
team = DevTeamAgents(LLM_CONFIG)
developer = team.get_agent("developer")

# Poser une question
team.user_proxy.initiate_chat(
    developer,
    message="Peux-tu créer une fonction de tri rapide en Python ?"
)
```

### Révision de Code

```python
from src.agents import CodeReviewWorkflow

# Créer le workflow
team = DevTeamAgents(LLM_CONFIG)
workflow = CodeReviewWorkflow(team)

# Lancer la révision
workflow.start_code_review(
    "Créer une classe pour gérer un cache LRU thread-safe"
)
```

### Discussion d'Équipe

```python
# Sélectionner les agents
selected_agents = ["developer", "reviewer", "tester"]
group_chat = team.create_group_chat(selected_agents)
manager = team.create_group_chat_manager(group_chat)

# Démarrer la discussion
team.user_proxy.initiate_chat(
    manager,
    message="Comment architecturer une API REST scalable ?"
)
```

## 🔧 Personnalisation

### Modifier les Agents

Éditez `src/config.py` pour personnaliser les agents :

```python
AGENT_CONFIGS = {
    "developer": {
        "system_message": "Votre nouveau message système...",
        "llm_config": LLM_CONFIG
    }
}
```

### Ajouter de Nouveaux Agents

```python
# Dans agents.py
self.agents["data_scientist"] = autogen.AssistantAgent(
    name="Data_Scientist",
    system_message="Expert en analyse de données...",
    llm_config=self.llm_config
)
```

### Créer des Workflows Personnalisés

```python
class CustomWorkflow:
    def __init__(self, team: DevTeamAgents):
        self.team = team
        # Votre logique personnalisée
    
    def start_custom_process(self, request: str):
        # Votre workflow personnalisé
        pass
```

## 🐛 Dépannage

### Diagnostic Rapide

```bash
# Test complet d'installation
python test_installation.py

# Vérification rapide
python -c "
import os
print('API Key:', '✅' if os.getenv('OPENAI_API_KEY') else '❌')
try:
    import autogen; print('AutoGen:', '✅')
except: print('AutoGen:', '❌')
try:
    from src.config import LLM_CONFIG; print('Config:', '✅')
except: print('Config:', '❌')
"
```

### Problèmes Courants

#### ❌ Clé API non configurée
```
Solution : Vérifiez votre fichier .env et la variable OPENAI_API_KEY
```

#### ❌ Erreur d'import autogen
```bash
# Réinstaller AutoGen
pip install --upgrade autogen-agentchat
```

#### ❌ Streamlit ne démarre pas
```bash
# Vérifier l'installation
pip install --upgrade streamlit
streamlit hello  # Test Streamlit
```

#### ❌ Agents ne répondent pas
```
Vérifications :
1. Clé API valide et avec crédit
2. Connexion internet stable  
3. Configuration LLM_CONFIG correcte
```

### Mode Debug

```python
# Activer les logs détaillés
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Support

- 📚 [Documentation AutoGen](https://github.com/microsoft/autogen)
- 🐛 Ouvrir une issue sur le repository
- 💬 Discussions dans la communauté AutoGen

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. 🍴 Fork le projet
2. 🌟 Créer une branche feature
3. 💍 Commit vos changements
4. 📤 Push vers la branche
5. 🔃 Ouvrir une Pull Request

---

**🚀 Bon développement avec vos agents IA !**
