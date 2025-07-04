"""
Script d'installation automatique pour le projet AutoGen Agents
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_command(command, description):
    """Exécuter une commande et afficher le résultat"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} réussi")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de {description}")
        print(f"   {e.stderr}")
        return False


def check_python_version():
    """Vérifier la version de Python"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} détecté")
        return True
    else:
        print(f"❌ Python 3.8+ requis, version actuelle : {version.major}.{version.minor}")
        return False


def check_pip():
    """Vérifier que pip est disponible"""
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      check=True, capture_output=True)
        print("✅ pip disponible")
        return True
    except subprocess.CalledProcessError:
        print("❌ pip non trouvé")
        return False


def install_dependencies():
    """Installer les dépendances Python"""
    requirements_file = Path("requirements.txt")
    if not requirements_file.exists():
        print("❌ Fichier requirements.txt non trouvé")
        return False
    
    return run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installation des dépendances"
    )


def setup_env_file():
    """Configurer le fichier d'environnement"""
    env_example = Path(".env.example")
    env_file = Path(".env")
    
    if not env_example.exists():
        print("❌ Fichier .env.example non trouvé")
        return False
    
    if env_file.exists():
        print("ℹ️  Fichier .env existe déjà")
        return True
    
    try:
        shutil.copy(env_example, env_file)
        print("✅ Fichier .env créé à partir de .env.example")
        print("📝 Veuillez éditer .env pour configurer votre clé API OpenAI")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la création du fichier .env : {e}")
        return False


def verify_installation():
    """Vérifier que l'installation fonctionne"""
    print("\n🔍 Vérification de l'installation...")
    
    try:
        # Test d'import AutoGen
        subprocess.run([sys.executable, "-c", "import autogen; print('AutoGen importé avec succès')"],
                      check=True, capture_output=True, text=True)
        print("✅ AutoGen fonctionne")
        
        # Test d'import des modules du projet
        subprocess.run([sys.executable, "-c", "from src.config import LLM_CONFIG; print('Configuration chargée')"],
                      check=True, capture_output=True, text=True)
        print("✅ Modules du projet accessibles")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la vérification : {e.stderr}")
        return False


def display_next_steps():
    """Afficher les prochaines étapes"""
    print("\n" + "="*60)
    print("🎉 INSTALLATION TERMINÉE !")
    print("="*60)
    print("\n📋 Prochaines étapes :")
    print("1. 🔑 Configurez votre clé API OpenAI dans le fichier .env")
    print("2. 🚀 Testez l'installation :")
    print("   - Interface terminal : python src/main.py")
    print("   - Interface web : streamlit run src/streamlit_app.py")
    print("   - Exemples : python examples/simple_chat.py")
    print("3. 📚 Consultez le README.md pour plus d'informations")
    print("\n🤖 Bon développement avec vos agents IA !")


def main():
    """Fonction principale d'installation"""
    print("🚀 INSTALLATION DU PROJET AUTOGEN AGENTS")
    print("="*60)
    
    # Vérifications préliminaires
    if not check_python_version():
        sys.exit(1)
    
    if not check_pip():
        sys.exit(1)
    
    # Installation
    success = True
    
    if not install_dependencies():
        success = False
    
    if not setup_env_file():
        success = False
    
    if success and not verify_installation():
        success = False
    
    # Résultats
    if success:
        display_next_steps()
    else:
        print("\n❌ L'installation a échoué. Veuillez vérifier les erreurs ci-dessus.")
        sys.exit(1)


if __name__ == "__main__":
    main()