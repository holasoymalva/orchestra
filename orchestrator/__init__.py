"""
Orchestra - Multi-Agent Orchestrator for AI systems
==================================================

Orchestra es un framework para crear y gestionar sistemas multi-agente donde
varios agentes de IA colaboran para resolver tareas complejas.

Características principales:
- Definir diferentes roles y capacidades para cada agente
- Establecer protocolos de comunicación entre agentes
- Visualizar el flujo de información y toma de decisiones
- Exportar el sistema como servicio API o aplicación
"""

from orchestra.messaging import Message, MessageType, Priority
from orchestra.agents import AgentInterface, FunctionalAgent, AgentState
from orchestra.orchestrator import MultiAgentOrchestrator
from orchestra.visualization import OrchestrationVisualizer
from orchestra.exporters import ApiExporter

__version__ = "0.1.0"
__author__ = "holasoymalva"

__all__ = [
    'Message',
    'MessageType',
    'Priority',
    'AgentInterface',
    'FunctionalAgent',
    'AgentState',
    'MultiAgentOrchestrator',
    'OrchestrationVisualizer',
    'ApiExporter',
]