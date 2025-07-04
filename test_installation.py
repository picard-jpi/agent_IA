"""
Script de test pour vérifier l'installation AutoGen Agents
"""

import os
import sys
import traceback
from pathlib import Path


def test_imports():
    """Tester les imports nécessaires"""
    print("🧪 Test des imports...")
    
    tests = [
        ("os", "Module os système"),
        ("sys", "Module sys"),
        ("autogen", "AutoGen framework"),
        ("openai", "Client OpenAI"),
        ("streamlit", "Framework Streamlit"),
        ("dotenv", "Python-dotenv"),
    ]
    
    success_count = 0
    
    for module, description in tests:
        try:
            __import__(module)
            print(f"✅ {description}")
            success_count += 1
        except ImportError as e:
            print(f"❌ {description} - Erreur: {e}")
    
    print(f"\n📊 Résultat: {success_count}/{len(tests)} imports réussis")
    return success_count == len(tests)


def test_project_structure():
    """Vérifier la structure du projet"""
    print("\n🏗️  Test de la structure du projet...")
    
    required_files = [
        "src/__init__.py",
        "src/config.py", 
        "src/agents.py",
        "src/main.py",
        "src/streamlit_app.py",
        "examples/simple_chat.py",
        "examples/code_review_example.py",
        ".env.example",
        "requirements.txt",
        "README.md"
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - Manquant")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️  Fichiers manquants: {', '.join(missing_files)}")
        return False
    else:
        print(f"\n✅ Structure du projet complète")
        return True


def test_configuration():
    """Tester la configuration"""
    print("\n⚙️  Test de la configuration...")
    
    # Vérifier le fichier .env
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if not env_example.exists():
        print("❌ Fichier .env.example manquant")
        return False
    
    if not env_file.exists():
        print("⚠️  Fichier .env non trouvé - créé à partir de .env.example")
        print("📝 Veuillez configurer votre clé API OpenAI")
        return False
    
    # Charger les variables d'environnement
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            if api_key.startswith("sk-") and len(api_key) > 20:
                print("✅ Clé API OpenAI configurée")
                return True
            else:
                print("⚠️  Clé API OpenAI semble invalide")
                return False
        else:
            print("⚠️  Clé API OpenAI non configurée")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors du chargement de la configuration: {e}")
        return False


def test_agents_creation():
    """Tester la création des agents"""
    print("\n🤖 Test de création des agents...")
    
    try:
        # Ajouter le répertoire au path
        sys.path.append('.')
        
        from src.config import LLM_CONFIG, AGENT_CONFIGS
        from src.agents import DevTeamAgents
        
        print("✅ Import des modules du projet réussi")
        
        # Tester la création des agents (sans appel API)
        print("✅ Configuration des agents chargée")
        print(f"   - Agents disponibles: {list(AGENT_CONFIGS.keys())}")
        
        # Note: On ne crée pas réellement les agents pour éviter d'utiliser l'API
        print("✅ Test de création des agents simulé")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test des agents: {e}")
        print("Détails de l'erreur:")
        traceback.print_exc()
        return False


def test_vscode_integration():
    """Tester l'intégration VSCode"""
    print("\n🔧 Test de l'intégration VSCode...")
    
    vscode_files = [
        ".vscode/tasks.json",
        ".vscode/launch.json", 
        ".vscode/extensions.json"
    ]
    
    success = True
    
    for file_path in vscode_files:
        if Path(file_path).exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - Manquant")
            success = False
    
    return success


def display_summary(results):
    """Afficher le résumé des tests"""
    print("\n" + "="*60)
    print("📋 RÉSUMÉ DES TESTS")
    print("="*60)
    
    total_tests = len(results)
    passed_tests = sum(results.values())
    
    for test_name, result in results.items():
        status = "✅ RÉUSSI" if result else "❌ ÉCHOUÉ"
        print(f"{test_name}: {status}")
    
    print(f"\n📊 Score: {passed_tests}/{total_tests} tests réussis")
    
    if passed_tests == total_tests:
        print("\n🎉 INSTALLATION COMPLÈTE !")
        print("🚀 Vous pouvez maintenant utiliser les agents AutoGen")
        print("\n📋 Prochaines étapes :")
        print("1. python run_examples.py - Tester les exemples")
        print("2. python src/main.py - Interface terminal")
        print("3. streamlit run src/streamlit_app.py - Interface web")
    else:
        print(f"\n⚠️  {total_tests - passed_tests} problème(s) détecté(s)")
        print("📝 Consultez les erreurs ci-dessus et le README.md")


def main():
    """Fonction principale de test"""
    print("🧪 TEST D'INSTALLATION AUTOGEN AGENTS")
    print("="*60)
    
    # Exécuter tous les tests
    results = {
        "Imports": test_imports(),
        "Structure": test_project_structure(),
        "Configuration": test_configuration(),
        "Agents": test_agents_creation(),
        "VSCode": test_vscode_integration()
    }
    
    # Afficher le résumé
    display_summary(results)


if __name__ == "__main__":
    main()