"""
Agents AutoGen spécialisés pour l'assistance au développement
"""

import autogen
from typing import Dict, List, Optional
from .config import AGENT_CONFIGS, USER_PROXY_CONFIG


class DevTeamAgents:
    """Classe principale pour gérer l'équipe d'agents de développement"""
    
    def __init__(self, llm_config: Optional[Dict] = None):
        self.llm_config = llm_config or AGENT_CONFIGS["developer"]["llm_config"]
        self.agents = {}
        self.user_proxy = None
        self._create_agents()
    
    def _create_agents(self):
        """Créer tous les agents de l'équipe"""
        
        # Agent développeur senior
        self.agents["developer"] = autogen.AssistantAgent(
            name=AGENT_CONFIGS["developer"]["name"],
            system_message=AGENT_CONFIGS["developer"]["system_message"],
            llm_config=self.llm_config
        )
        
        # Agent réviseur de code
        self.agents["reviewer"] = autogen.AssistantAgent(
            name=AGENT_CONFIGS["reviewer"]["name"],
            system_message=AGENT_CONFIGS["reviewer"]["system_message"],
            llm_config=self.llm_config
        )
        
        # Agent testeur
        self.agents["tester"] = autogen.AssistantAgent(
            name=AGENT_CONFIGS["tester"]["name"],
            system_message=AGENT_CONFIGS["tester"]["system_message"],
            llm_config=self.llm_config
        )
        
        # Agent chef de projet
        self.agents["project_manager"] = autogen.AssistantAgent(
            name=AGENT_CONFIGS["project_manager"]["name"],
            system_message=AGENT_CONFIGS["project_manager"]["system_message"],
            llm_config=self.llm_config
        )
        
        # Proxy utilisateur pour l'interaction
        self.user_proxy = autogen.UserProxyAgent(
            name=USER_PROXY_CONFIG["name"],
            human_input_mode=USER_PROXY_CONFIG["human_input_mode"],
            max_consecutive_auto_reply=USER_PROXY_CONFIG["max_consecutive_auto_reply"],
            code_execution_config=USER_PROXY_CONFIG["code_execution_config"]
        )
    
    def get_agent(self, agent_name: str) -> autogen.Agent:
        """Récupérer un agent spécifique"""
        if agent_name in self.agents:
            return self.agents[agent_name]
        raise ValueError(f"Agent '{agent_name}' non trouvé")
    
    def get_all_agents(self) -> List[autogen.Agent]:
        """Récupérer tous les agents"""
        return list(self.agents.values())
    
    def create_group_chat(self, agents: Optional[List[str]] = None) -> autogen.GroupChat:
        """Créer un groupe de discussion avec les agents spécifiés"""
        if agents is None:
            agents = list(self.agents.keys())
        
        selected_agents = [self.agents[agent] for agent in agents if agent in self.agents]
        selected_agents.append(self.user_proxy)
        
        return autogen.GroupChat(
            agents=selected_agents,
            messages=[],
            max_round=10,
            speaker_selection_method="round_robin"
        )
    
    def create_group_chat_manager(self, group_chat: autogen.GroupChat) -> autogen.GroupChatManager:
        """Créer un gestionnaire de groupe de discussion"""
        return autogen.GroupChatManager(
            groupchat=group_chat,
            llm_config=self.llm_config
        )


class CodeReviewWorkflow:
    """Workflow spécialisé pour la révision de code"""
    
    def __init__(self, team: DevTeamAgents):
        self.team = team
        self.developer = team.get_agent("developer")
        self.reviewer = team.get_agent("reviewer")
        self.tester = team.get_agent("tester")
        self.user_proxy = team.user_proxy
    
    def start_code_review(self, code_request: str):
        """Démarrer un processus de révision de code"""
        # Créer un groupe de discussion pour la révision
        group_chat = autogen.GroupChat(
            agents=[self.developer, self.reviewer, self.tester, self.user_proxy],
            messages=[],
            max_round=15,
            speaker_selection_method="round_robin"
        )
        
        manager = autogen.GroupChatManager(
            groupchat=group_chat,
            llm_config=self.team.llm_config
        )
        
        # Démarrer la conversation
        self.user_proxy.initiate_chat(
            manager,
            message=f"""Bonjour l'équipe ! J'ai besoin d'aide pour le développement suivant :

{code_request}

Processus souhaité :
1. Le développeur senior propose une solution
2. Le réviseur analyse le code et suggère des améliorations
3. L'ingénieur test crée les tests appropriés
4. Nous itérons jusqu'à obtenir une solution satisfaisante

Commençons !"""
        )


class ProjectPlanningWorkflow:
    """Workflow pour la planification de projet"""
    
    def __init__(self, team: DevTeamAgents):
        self.team = team
        self.project_manager = team.get_agent("project_manager")
        self.developer = team.get_agent("developer")
        self.user_proxy = team.user_proxy
    
    def start_project_planning(self, project_description: str):
        """Démarrer la planification d'un projet"""
        group_chat = autogen.GroupChat(
            agents=[self.project_manager, self.developer, self.user_proxy],
            messages=[],
            max_round=10,
            speaker_selection_method="round_robin"
        )
        
        manager = autogen.GroupChatManager(
            groupchat=group_chat,
            llm_config=self.team.llm_config
        )
        
        self.user_proxy.initiate_chat(
            manager,
            message=f"""Nouvelle demande de projet :

{project_description}

Chef de projet, pouvez-vous analyser cette demande et proposer un plan d'action avec l'aide du développeur senior ?"""
        )