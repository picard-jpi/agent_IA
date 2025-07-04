"""
Package principal pour les agents AutoGen
"""

from .config import LLM_CONFIG, AGENT_CONFIGS
from .agents import DevTeamAgents, CodeReviewWorkflow, ProjectPlanningWorkflow

__version__ = "1.0.0"
__all__ = ["DevTeamAgents", "CodeReviewWorkflow", "ProjectPlanningWorkflow", "LLM_CONFIG", "AGENT_CONFIGS"]