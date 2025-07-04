# 🤖 Cas d'Usage AutoGen : Agents AI Collaboratifs

Ce projet démontre l'utilisation de **Microsoft AutoGen** pour créer des équipes d'agents AI spécialisés qui collaborent sur des tâches complexes.

## 🎯 Cas d'Usage Présentés

### 1. 🏢 Équipe de Planification Projet (Complexe)
Une simulation complète d'équipe projet avec 6 agents spécialisés :
- **Chef de Projet** : Coordination et vision globale
- **Développeur Backend** : Architecture technique serveur
- **Développeur Frontend/Mobile** : Interface utilisateur
- **Designer UX/UI** : Expérience utilisateur
- **Ingénieur QA** : Tests et qualité
- **Critique/Reviewer** : Évaluation externe

**Scénario** : Planification d'une application mobile de fitness social

### 2. 🔍 Analyse Collaborative (Simple)
Collaboration entre 2 agents experts :
- **Analyste de Données** : Analyse statistique et insights
- **Expert Visualisation** : Recommandations graphiques et dashboards

**Scénario** : Analyse de performance e-commerce

## 🚀 Installation

### 1. Prérequis
```bash
# Python 3.8+ requis
python --version
```

### 2. Installation des dépendances
```bash
# Installer les packages requis
pip install -r requirements.txt
```

### 3. Configuration API OpenAI
```bash
# Copier le template de configuration
cp .env.template .env

# Éditer le fichier .env avec votre clé API
# OPENAI_API_KEY=sk-votre_cle_api_ici
```

**Obtenir une clé API OpenAI :**
1. Aller sur [platform.openai.com](https://platform.openai.com/api-keys)
2. Créer un compte ou se connecter
3. Générer une nouvelle clé API
4. Copier la clé dans le fichier `.env`

## 🎮 Utilisation

### Lancement Principal
```bash
python simple_agents_example.py
```

Le script propose un menu pour choisir l'exemple :
- **Option 1** : Équipe complète de planification projet
- **Option 2** : Analyse collaborative simple

### Lancement Direct des Exemples

#### Équipe de Planification Projet
```bash
python project_planning_agents.py
```

#### Analyse Simple
```bash
python simple_agents_example.py
# Puis choisir l'option 2
```

## 📁 Structure du Projet

```
├── project_planning_agents.py   # Exemple complexe - équipe projet
├── simple_agents_example.py     # Exemple simple + menu principal  
├── requirements.txt             # Dépendances Python
├── .env.template               # Template configuration
├── .env                        # Configuration API (à créer)
└── README.md                   # Documentation
```

## 🔧 Fonctionnalités AutoGen Démontrées

### Communication Multi-Agents
- **GroupChat** : Conversation de groupe avec rotation des participants
- **Initiate Chat** : Communication directe entre deux agents
- **Speaker Selection** : Gestion automatique de la prise de parole

### Types d'Agents
- **AssistantAgent** : Agents spécialisés avec prompts système
- **UserProxyAgent** : Interface utilisateur et proxy
- **GroupChatManager** : Coordination des conversations de groupe

### Configuration LLM
- Support GPT-4 et GPT-3.5-turbo
- Paramètres de température et timeout
- Gestion des erreurs API

## 🎨 Personnalisation

### Modifier les Agents
Dans `project_planning_agents.py`, vous pouvez :
- Ajuster les `system_message` des agents
- Changer les spécialisations
- Ajouter de nouveaux agents à l'équipe

### Changer le Scénario
- Modifier la variable `project_brief` avec votre cas d'usage
- Adapter les contraintes et objectifs
- Ajuster les questions posées aux agents

### Paramètres de Conversation
```python
group_chat = autogen.GroupChat(
    agents=agents_list,
    messages=[],
    max_round=12,           # Nombre max d'échanges
    speaker_selection_method="round_robin"  # ou "auto"
)
```

## 🔍 Exemples de Sortie

### Équipe de Planification
Les agents vont collaborer pour :
- Analyser la faisabilité du projet
- Proposer une architecture technique
- Définir l'expérience utilisateur
- Planifier les phases de développement
- Identifier les risques et mitigation

### Analyse Collaborative  
Les experts vont :
- Interpréter les métriques business
- Identifier les problèmes de performance
- Recommander des visualisations efficaces
- Proposer des actions d'amélioration

## 🚨 Dépannage

### Erreur "OPENAI_API_KEY manquante"
- Vérifier que le fichier `.env` existe
- S'assurer que la clé API est correctement formatée
- Tester la clé sur [platform.openai.com](https://platform.openai.com)

### Erreur de connexion API
- Vérifier votre connexion internet
- Contrôler le solde de votre compte OpenAI
- Augmenter le `timeout` dans la config LLM

### Import AutoGen échoue
```bash
# Réinstaller AutoGen
pip uninstall pyautogen
pip install pyautogen>=0.2.0
```

## 💡 Idées d'Extension

1. **Nouveaux Domaines**
   - Équipe de marketing digital
   - Conseil en investissement
   - Analyse juridique collaborative

2. **Fonctionnalités Avancées**
   - Intégration avec des APIs externes
   - Sauvegarde des conversations
   - Interface web avec Streamlit

3. **Agents Spécialisés**
   - Agent avec accès à une base de données
   - Agent capable d'exécuter du code
   - Agent avec recherche web

## 📚 Ressources

- [Documentation AutoGen](https://microsoft.github.io/autogen/)
- [Exemples AutoGen GitHub](https://github.com/microsoft/autogen/tree/main/notebook)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🏷️ Tags
`#AutoGen` `#MultiAgent` `#AI` `#Collaboration` `#OpenAI` `#Python` `#LLM`
