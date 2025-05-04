"""
Definición de mensajes y tipos para el sistema multi-agente.
"""

import uuid
import datetime
from enum import Enum
from typing import Dict, Any, Optional
from dataclasses import dataclass, field, asdict

# Clase para el tipo de mensaje
class MessageType(str, Enum):
    QUERY = "query"
    RESPONSE = "response"
    COMMAND = "command"
    ERROR = "error"
    INFO = "info"
    SYSTEM = "system"

# Clase para definir el nivel de prioridad de un mensaje
class Priority(int, Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3

# Definición de un mensaje entre agentes
@dataclass
class Message:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    sender_id: str
    receiver_id: Optional[str] = None
    content: Any = None
    msg_type: MessageType = MessageType.INFO
    timestamp: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    priority: Priority = Priority.MEDIUM
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte el mensaje a un diccionario."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Message':
        """Crea un mensaje a partir de un diccionario."""
        # Convertir enums de string a objeto enum
        if isinstance(data.get('msg_type'), str):
            data['msg_type'] = MessageType(data['msg_type'])
        if isinstance(data.get('priority'), int):
            data['priority'] = Priority(data['priority'])
        return cls(**data)