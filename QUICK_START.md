# 🚀 Démarrage Rapide AutoGen

## Installation Express

```bash
# 1. Exécuter le script d'installation
./setup.sh

# 2. Activer l'environnement
source autogen_env/bin/activate

# 3. Configurer l'API OpenAI
cp .env.template .env
# Éditer .env avec votre clé API OpenAI

# 4. Lancer les exemples
python simple_agents_example.py
```

## 🔑 Obtenir une Clé API OpenAI

1. Aller sur [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Se connecter ou créer un compte
3. Cliquer "Create new secret key"
4. Copier la clé dans `.env`

## 🎮 Exemples Disponibles

### 1. Équipe de Planification Projet
- **6 agents spécialisés** collaborent sur un projet
- Chef de projet, développeurs, designer, QA, reviewer
- **Scénario**: App mobile de fitness social

### 2. Analyse Collaborative Simple  
- **2 agents experts** analysent des données business
- Analyste de données + Expert visualisation
- **Scénario**: Performance e-commerce

### 3. Agents avec Exécution de Code
- **3 agents** qui peuvent exécuter du Python
- Data scientist + Exécuteur + Validateur
- **Scénario**: Analyse de données automatisée

## 🔧 Structure des Fichiers

```
├── project_planning_agents.py    # Exemple complexe
├── simple_agents_example.py      # Menu principal + exemple simple
├── advanced_code_agents.py       # Agents avec code
├── requirements.txt              # Dépendances
├── setup.sh                      # Installation automatique
├── .env.template                 # Template configuration
└── README.md                     # Documentation complète
```

## 🐛 Dépannage Express

**Erreur API Key**: Vérifiez votre fichier `.env`
**Erreur Import**: Activez l'environnement virtuel
**Erreur Connexion**: Vérifiez votre crédit OpenAI

## 💡 Personnalisation Rapide

**Changer le scénario**: Modifier `project_brief` dans les scripts
**Nouveaux agents**: Ajouter dans `create_agents()`
**Autres modèles**: Ajuster `config_list` dans setup functions

---
📖 **Pour plus de détails**: `README.md`