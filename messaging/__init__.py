"""
Módulo de mensajería para Orchestra.

Este módulo contiene las clases y funciones relacionadas con la gestión
de mensajes entre agentes en el sistema multi-agente.
"""

from orchestra.messaging.message import Message, MessageType, Priority

__all__ = [
    'Message',
    'MessageType',
    'Priority',
]