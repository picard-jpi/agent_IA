"""
Interface web Streamlit pour les agents AutoGen
"""

import streamlit as st
import os
import sys
from io import StringIO
import contextlib

# Ajouter le répertoire parent au path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents import DevTeamAgents, CodeReviewWorkflow, ProjectPlanningWorkflow
from src.config import LLM_CONFIG


# Configuration de la page
st.set_page_config(
    page_title="Agents IA AutoGen",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_resource
def initialize_team():
    """Initialiser l'équipe d'agents (mise en cache)"""
    if not os.getenv("OPENAI_API_KEY"):
        st.error("❌ OPENAI_API_KEY n'est pas configurée. Veuillez configurer votre clé API.")
        st.stop()
    
    return DevTeamAgents(LLM_CONFIG)


def capture_output(func, *args, **kwargs):
    """Capturer la sortie d'une fonction pour l'affichage dans Streamlit"""
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    
    captured_output = StringIO()
    
    try:
        sys.stdout = captured_output
        sys.stderr = captured_output
        
        result = func(*args, **kwargs)
        
        return result, captured_output.getvalue()
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr


def main():
    """Interface principale Streamlit"""
    
    # Titre principal
    st.title("🤖 Système d'Agents IA avec AutoGen")
    st.markdown("---")
    
    # Sidebar pour la configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Vérification de la clé API
        api_key_status = "✅ Configurée" if os.getenv("OPENAI_API_KEY") else "❌ Non configurée"
        st.info(f"Clé API OpenAI : {api_key_status}")
        
        # Informations sur les agents
        st.header("👥 Agents Disponibles")
        st.write("🧑‍💻 **Développeur Senior**")
        st.caption("Code propre et solutions techniques")
        
        st.write("🔍 **Réviseur de Code**")
        st.caption("Analyse qualité et améliorations")
        
        st.write("🧪 **Ingénieur Test**")
        st.caption("Tests et couverture de code")
        
        st.write("📋 **Chef de Projet**")
        st.caption("Coordination et planification")
    
    # Onglets principaux
    tab1, tab2, tab3 = st.tabs(["💻 Révision de Code", "📋 Planification Projet", "💬 Discussion Libre"])
    
    # Initialiser l'équipe
    try:
        team = initialize_team()
    except Exception as e:
        st.error(f"Erreur lors de l'initialisation : {e}")
        return
    
    # Onglet Révision de Code
    with tab1:
        st.header("💻 Révision de Code Collaborative")
        st.write("Travaillez avec une équipe d'agents pour développer et réviser du code.")
        
        code_request = st.text_area(
            "📝 Décrivez le code que vous souhaitez développer :",
            placeholder="Exemple : Créer une fonction pour calculer la factorielle avec gestion d'erreurs",
            height=100
        )
        
        col1, col2 = st.columns([1, 4])
        
        with col1:
            if st.button("🚀 Lancer la révision", type="primary"):
                if code_request.strip():
                    with st.spinner("🔄 Révision en cours..."):
                        workflow = CodeReviewWorkflow(team)
                        
                        # Placeholder pour simuler l'interaction
                        st.success("✅ Révision de code initialisée !")
                        st.info("💡 Dans un environnement réel, la conversation interactive démarrerait ici.")
                        
                        # Afficher le message qui serait envoyé
                        with st.expander("📋 Message envoyé à l'équipe"):
                            st.code(f"""Bonjour l'équipe ! J'ai besoin d'aide pour le développement suivant :

{code_request}

Processus souhaité :
1. Le développeur senior propose une solution
2. Le réviseur analyse le code et suggère des améliorations  
3. L'ingénieur test crée les tests appropriés
4. Nous itérons jusqu'à obtenir une solution satisfaisante

Commençons !""")
                else:
                    st.warning("⚠️ Veuillez décrire votre demande de code")
    
    # Onglet Planification Projet
    with tab2:
        st.header("📋 Planification de Projet")
        st.write("Planifiez votre projet avec l'aide du chef de projet et du développeur senior.")
        
        project_description = st.text_area(
            "📝 Décrivez votre projet :",
            placeholder="Exemple : Application web de gestion de tâches avec authentification utilisateur",
            height=100
        )
        
        col1, col2 = st.columns([1, 4])
        
        with col1:
            if st.button("📋 Planifier le projet", type="primary"):
                if project_description.strip():
                    with st.spinner("🔄 Planification en cours..."):
                        workflow = ProjectPlanningWorkflow(team)
                        
                        st.success("✅ Planification de projet initialisée !")
                        st.info("💡 Dans un environnement réel, la conversation interactive démarrerait ici.")
                        
                        with st.expander("📋 Message envoyé à l'équipe"):
                            st.code(f"""Nouvelle demande de projet :

{project_description}

Chef de projet, pouvez-vous analyser cette demande et proposer un plan d'action avec l'aide du développeur senior ?""")
                else:
                    st.warning("⚠️ Veuillez décrire votre projet")
    
    # Onglet Discussion Libre
    with tab3:
        st.header("💬 Discussion Libre avec l'Équipe")
        st.write("Discutez librement avec les agents de votre choix.")
        
        # Sélection des agents
        st.subheader("👥 Sélection des Agents")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            dev_selected = st.checkbox("🧑‍💻 Développeur", value=True)
        with col2:
            reviewer_selected = st.checkbox("🔍 Réviseur", value=True)
        with col3:
            tester_selected = st.checkbox("🧪 Testeur", value=False)
        with col4:
            pm_selected = st.checkbox("📋 Chef Projet", value=False)
        
        # Message
        message = st.text_area(
            "📝 Votre message à l'équipe :",
            placeholder="Posez votre question ou décrivez votre problème...",
            height=100
        )
        
        col1, col2 = st.columns([1, 4])
        
        with col1:
            if st.button("💬 Envoyer", type="primary"):
                selected_agents = []
                if dev_selected:
                    selected_agents.append("developer")
                if reviewer_selected:
                    selected_agents.append("reviewer")
                if tester_selected:
                    selected_agents.append("tester")
                if pm_selected:
                    selected_agents.append("project_manager")
                
                if not selected_agents:
                    st.warning("⚠️ Veuillez sélectionner au moins un agent")
                elif not message.strip():
                    st.warning("⚠️ Veuillez saisir un message")
                else:
                    with st.spinner("🔄 Discussion en cours..."):
                        st.success("✅ Discussion initialisée !")
                        st.info(f"💡 Agents sélectionnés : {', '.join(selected_agents)}")
                        st.info("💡 Dans un environnement réel, la conversation interactive démarrerait ici.")
                        
                        with st.expander("📋 Configuration de la discussion"):
                            st.write(f"**Agents participants :** {', '.join(selected_agents)}")
                            st.write(f"**Message initial :** {message}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        🤖 Système d'Agents AutoGen - Version 1.0.0<br>
        Développé pour VSCode avec interface web Streamlit
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()