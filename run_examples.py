"""
Script pour exécuter les exemples facilement
"""

import os
import sys
import subprocess
from pathlib import Path


def check_api_key():
    """Vérifier si la clé API est configurée"""
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY n'est pas configurée")
        print("📝 Veuillez configurer votre clé API dans le fichier .env")
        return False
    return True


def run_example(script_path, description):
    """Exécuter un exemple spécifique"""
    print(f"\n🚀 Lancement : {description}")
    print("="*50)
    
    try:
        subprocess.run([sys.executable, script_path], check=True)
        print(f"✅ {description} terminé")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'exécution de {description}")
        print(f"   Code de sortie : {e.returncode}")
    except KeyboardInterrupt:
        print(f"\n⏹️  Arrêt de {description}")


def display_menu():
    """Afficher le menu des exemples"""
    print("\n" + "="*60)
    print("🤖 EXEMPLES AUTOGEN AGENTS")
    print("="*60)
    print("1. 💬 Chat simple avec un agent")
    print("2. 🔍 Révision de code collaborative")
    print("3. 🖥️  Interface terminal interactive")
    print("4. 🌐 Interface web Streamlit")
    print("5. 📓 Notebook Jupyter")
    print("6. 🚪 Quitter")
    print("="*60)


def main():
    """Fonction principale"""
    print("🎯 Sélecteur d'Exemples AutoGen")
    
    # Vérifier la configuration
    if not check_api_key():
        return
    
    while True:
        display_menu()
        
        try:
            choice = input("\n👉 Votre choix (1-6) : ").strip()
            
            if choice == "1":
                run_example("examples/simple_chat.py", "Chat Simple")
                
            elif choice == "2":
                run_example("examples/code_review_example.py", "Révision de Code")
                
            elif choice == "3":
                run_example("src/main.py", "Interface Terminal")
                
            elif choice == "4":
                print("\n🌐 Lancement de l'interface web Streamlit...")
                print("🔗 Accédez à http://localhost:8501 dans votre navigateur")
                try:
                    subprocess.run(["streamlit", "run", "src/streamlit_app.py"], check=True)
                except KeyboardInterrupt:
                    print("\n⏹️  Arrêt de Streamlit")
                except subprocess.CalledProcessError:
                    print("❌ Erreur lors du lancement de Streamlit")
                    print("💡 Assurez-vous que Streamlit est installé : pip install streamlit")
                    
            elif choice == "5":
                print("\n📓 Lancement de Jupyter...")
                try:
                    subprocess.run(["jupyter", "notebook", "notebooks/"], check=True)
                except KeyboardInterrupt:
                    print("\n⏹️  Arrêt de Jupyter")
                except subprocess.CalledProcessError:
                    print("❌ Erreur lors du lancement de Jupyter")
                    print("💡 Assurez-vous que Jupyter est installé : pip install jupyter")
                    
            elif choice == "6":
                print("\n👋 Au revoir !")
                break
                
            else:
                print("❌ Choix invalide, veuillez sélectionner 1-6")
                
        except KeyboardInterrupt:
            print("\n\n👋 Arrêt du programme")
            break
        except Exception as e:
            print(f"\n❌ Erreur : {e}")


if __name__ == "__main__":
    main()