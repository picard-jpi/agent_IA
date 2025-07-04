#!/bin/bash

echo "🚀 Configuration de l'environnement AutoGen"
echo "==========================================="

# Vérification de Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    exit 1
fi

# Installation des packages système nécessaires
echo "📦 Installation des dépendances système..."
sudo apt update
sudo apt install -y python3-venv python3-pip

# Création de l'environnement virtuel
echo "🔧 Création de l'environnement virtuel..."
python3 -m venv autogen_env

# Activation et installation des dépendances
echo "📚 Installation des packages Python..."
source autogen_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Installation terminée!"
echo ""
echo "🎯 Pour utiliser AutoGen:"
echo "1. Activez l'environnement: source autogen_env/bin/activate"
echo "2. Configurez votre clé API: cp .env.template .env"
echo "3. Éditez .env avec votre clé OpenAI"
echo "4. Lancez: python simple_agents_example.py"
echo ""
echo "📖 Lisez le README.md pour plus d'informations"