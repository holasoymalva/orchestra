# 🎭 Orchestra - Multi-Agent Orchestrator

Orchestra es un framework de Python diseñado para crear, gestionar y orquestar sistemas multi-agente donde diversos agentes de IA colaboran para resolver tareas complejas.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![GitHub License](https://img.shields.io/github/license/holasoymalva/orchestra)](https://github.com/holasoymalva/orchestra/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/holasoymalva/orchestra/pulls)

## 🌟 Características

Orchestra ofrece un conjunto completo de herramientas para construir sistemas multi-agente sofisticados:

- **👤 Roles y Capacidades Personalizadas**: Define distintos roles y capacidades para cada agente.
- **💬 Comunicación Inter-Agente**: Configura protocolos robustos de comunicación entre agentes.
- **📊 Visualización del Flujo**: Visualiza el flujo de información y la toma de decisiones.
- **🔌 API REST Integrada**: Expone tu sistema como un servicio API REST.
- **📦 Exportación/Importación**: Guarda y carga configuraciones del sistema.
- **🔄 Procesamiento Asíncrono**: Maneja tareas en paralelo con procesamiento asíncrono.

## 🔍 Diagrama del Sistema

## 🚀 Instalación

### Requisitos

- Python 3.8 o superior
- pip (administrador de paquetes de Python)

### Configuración del Entorno Virtual

La forma recomendada de instalar Orchestra es usando un entorno virtual:

```bash
# Clonar el repositorio
git clone https://github.com/holasoymalva/orchestra.git
cd orchestra

# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar las dependencias
pip install -r requirements.txt
```

### Instalación Directa desde PyPI

Alternativamente, puedes instalar Orchestra directamente desde PyPI:

```bash
pip install multi-agent-orchestra
```

## 📋 Requisitos

Las dependencias principales se encuentran en el archivo `requirements.txt`:

```
asyncio>=3.4.3
networkx>=2.8.0
matplotlib>=3.5.1
fastapi>=0.85.0
uvicorn>=0.18.3
pydantic>=1.9.0
```

## 🎮 Uso Básico

A continuación se muestra un ejemplo básico de cómo crear un sistema multi-agente:

```python
import asyncio
from orchestra import MultiAgentOrchestrator, FunctionalAgent, Message, MessageType

# Crear el orchestrator
orchestrator = MultiAgentOrchestrator(name="Sistema de Análisis de Datos")

# Definir funciones de procesamiento para los agentes
async def data_collector_process(message):
    # Simular recolección de datos
    data = {"temperatura": 22.5, "humedad": 60, "presión": 1013}
    return Message(
        sender_id="recolector",
        receiver_id="analizador",
        content=data,
        msg_type=MessageType.INFO
    )

async def data_analyzer_process(message):
    # Analizar los datos recibidos
    data = message.content
    analysis = {"promedio": sum(data.values()) / len(data), "estado": "normal"}
    return Message(
        sender_id="analizador",
        receiver_id="reportero",
        content=analysis,
        msg_type=MessageType.INFO
    )

async def report_generator_process(message):
    # Generar un reporte
    analysis = message.content
    report = f"Reporte: Valores promedio de {analysis['promedio']:.2f}, estado {analysis['estado']}"
    print(report)
    return None

# Crear los agentes
recolector = FunctionalAgent(
    name="Recolector de Datos",
    role="data_collection",
    process_func=data_collector_process,
    capabilities=["sensing", "data_gathering"]
)

analizador = FunctionalAgent(
    name="Analizador",
    role="data_analysis",
    process_func=data_analyzer_process,
    capabilities=["statistics", "pattern_recognition"]
)

reportero = FunctionalAgent(
    name="Generador de Reportes",
    role="reporting",
    process_func=report_generator_process,
    capabilities=["formatting", "visualization"]
)

# Configurar IDs personalizados
recolector.id = "recolector"
analizador.id = "analizador"
reportero.id = "reportero"

# Agregar los agentes al orchestrator
orchestrator.add_agent(recolector)
orchestrator.add_agent(analizador)
orchestrator.add_agent(reportero)

# Función principal asíncrona
async def main():
    # Iniciar el orchestrator
    await orchestrator.start()
    
    # Enviar un mensaje para iniciar el flujo
    inicio_message = Message(
        sender_id="system",
        receiver_id="recolector",
        content="Iniciar recolección",
        msg_type=MessageType.COMMAND
    )
    await orchestrator.send_message(inicio_message)
    
    # Esperar a que se procesen los mensajes
    await asyncio.sleep(2)
    
    # Visualizar el sistema
    orchestrator.visualize(save_path="flujo_sistema.png")
    
    # Detener el orchestrator
    await orchestrator.stop()

# Ejecutar el flujo
if __name__ == "__main__":
    asyncio.run(main())
```

## 🖥️ Exportación como API

Orchestra permite exportar fácilmente tu sistema multi-agente como una API REST:

```python
from orchestra import ApiExporter

# Crear el orchestrator y configurar agentes (como en el ejemplo anterior)
# ...

# Exportar como API
api_exporter = ApiExporter(orchestrator)

# Iniciar el servidor (por defecto en http://localhost:8000)
api_exporter.run()
```

Una vez iniciado, puedes acceder a la documentación de la API en `http://localhost:8000/docs`.

## 📊 Visualización

Orchestra proporciona herramientas integradas para visualizar el flujo de información:

```python
# Generar una visualización del sistema
orchestrator.visualize(figsize=(12, 8), save_path="mi_sistema.png")

# Obtener estadísticas del flujo de mensajes
stats = orchestrator.visualizer.get_message_flow_stats()
print(stats)
```

## 🧩 Estructura del Proyecto

```
orchestra/
├── __init__.py
├── agents/
│   ├── __init__.py
│   ├── base.py              # Interfaces y clases base para agentes
│   ├── functional.py        # Implementación de agentes funcionales
│   └── specialized/         # Agentes especializados
├── messaging/
│   ├── __init__.py
│   ├── message.py           # Definición de mensajes y tipos
│   └── queue.py             # Implementación de colas de mensajes
├── orchestrator/
│   ├── __init__.py
│   └── core.py              # Implementación principal del orchestrator
├── visualization/
│   ├── __init__.py
│   └── visualizer.py        # Herramientas de visualización
└── exporters/
    ├── __init__.py
    ├── api.py               # Exportador de API
    └── json.py              # Exportación/importación en formato JSON
```

## 📝 Ejemplos

Explora ejemplos más detallados en el directorio `/examples`:

- **Sistema de Procesamiento de Datos**: Implementación de un flujo de recolección y análisis.
- **Chatbot Multi-Agente**: Sistema conversacional con agentes especializados.
- **Sistema de Recomendaciones**: Agentes colaborativos para generar recomendaciones.

## 🤝 Contribuir

Las contribuciones son bienvenidas! Si quieres contribuir:

1. Haz fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios
4. Ejecuta las pruebas (`pytest`)
5. Haz commit de tus cambios (`git commit -m 'Añadir nueva funcionalidad'`)
6. Sube los cambios a tu fork (`git push origin feature/nueva-funcionalidad`)
7. Abre un Pull Request

Por favor, asegúrate de seguir nuestro [Código de Conducta](https://github.com/holasoymalva/orchestra/blob/main/CODE_OF_CONDUCT.md).

## 📄 Licencia

Este proyecto está licenciado bajo la [MIT License](https://github.com/holasoymalva/orchestra/blob/main/LICENSE).

## 📞 Contacto

Para preguntas, sugerencias o problemas, por favor:

- Abre un [issue](https://github.com/holasoymalva/orchestra/issues)
- Contacta al mantenedor: [holasoymalva](https://github.com/holasoymalva)

---

Construido con ❤️ por la comunidad. ¡Únete y contribuye!
