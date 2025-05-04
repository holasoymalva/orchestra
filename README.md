# 🎭 Orchestra - Multi-Agent Orchestrator

Orchestra is a Python framework designed to create, manage, and orchestrate multi-agent systems where various AI agents collaborate to solve complex tasks.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![GitHub License](https://img.shields.io/github/license/holasoymalva/orchestra)](https://github.com/holasoymalva/orchestra/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/holasoymalva/orchestra/pulls)

## 🌟 Features

Orchestra provides a comprehensive set of tools for building sophisticated multi-agent systems:

* **👤 Custom Roles and Capabilities**: Define different roles and capabilities for each agent.
* **💬 Inter-Agent Communication**: Set up robust communication protocols between agents.
* **📊 Flow Visualization**: Visualize information flow and decision-making.
* **🔌 Integrated REST API**: Expose your system as a REST API service.
* **📦 Export/Import**: Save and load system configurations.
* **🔄 Asynchronous Processing**: Handle tasks in parallel with asynchronous processing.

## 🔍 System Architecture

Orchestra’s architecture is based on modular components that interact with each other:

1. **MultiAgentOrchestrator**: The central core that manages the entire system.
2. **Agents**: Autonomous entities with specific roles and capabilities.
3. **Messaging System**: Facilitates structured communication between agents.
4. **Visualizer**: Tools to visualize the flow of information and statistics.
5. **Exporters**: Mechanisms to export the system in different formats.

## 🚀 Installation

### Quick Setup

The easiest way to get started is by using the automatic setup scripts:

**On Linux/Mac:**

```bash
# Grant execution permissions to the script
chmod +x setup_venv.sh

# Run the script
./setup_venv.sh
```

**On Windows:**

```batch
setup_venv.bat
```

These scripts:

* Create a virtual environment
* Install all dependencies
* Set up the package in development mode
* Verify the installation

### Manual Setup

If you prefer manual setup:

```bash
# Clone the repository
git clone https://github.com/holasoymalva/orchestra.git
cd orchestra

# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

### Install Directly from PyPI

Alternatively, you can install Orchestra directly from PyPI:

```bash
pip install orchestra
```

## 📋 Requirements

The main dependencies are listed in the `requirements.txt` file:

```
asyncio>=3.4.3
networkx>=2.8.0
matplotlib>=3.5.1
fastapi>=0.85.0
uvicorn>=0.18.3
pydantic>=1.9.0
python-dateutil>=2.8.2
typing-extensions>=4.0.0
```

## 🎮 Basic Usage

Here’s a basic example of how to create a multi-agent system:

```python
import asyncio
from orchestra import MultiAgentOrchestrator, FunctionalAgent, Message, MessageType

# Create the orchestrator
orchestrator = MultiAgentOrchestrator(name="Data Analysis System")

# Define processing functions for the agents
async def data_collector_process(message):
    # Simulate data collection
    data = {"temperature": 22.5, "humidity": 60, "pressure": 1013}
    return Message(
        sender_id="collector",
        receiver_id="analyzer",
        content=data,
        msg_type=MessageType.INFO
    )

async def data_analyzer_process(message):
    # Analyze the received data
    data = message.content
    analysis = {"average": sum(data.values()) / len(data), "status": "normal"}
    return Message(
        sender_id="analyzer",
        receiver_id="reporter",
        content=analysis,
        msg_type=MessageType.INFO
    )

async def report_generator_process(message):
    # Generate a report
    analysis = message.content
    report = f"Report: Average value {analysis['average']:.2f}, status {analysis['status']}"
    print(report)
    return None

# Create the agents
collector = FunctionalAgent(
    name="Data Collector",
    role="data_collection",
    process_func=data_collector_process,
    capabilities=["sensing", "data_gathering"]
)

analyzer = FunctionalAgent(
    name="Analyzer",
    role="data_analysis",
    process_func=data_analyzer_process,
    capabilities=["statistics", "pattern_recognition"]
)

reporter = FunctionalAgent(
    name="Report Generator",
    role="reporting",
    process_func=report_generator_process,
    capabilities=["formatting", "visualization"]
)

# Set custom IDs
collector.id = "collector"
analyzer.id = "analyzer"
reporter.id = "reporter"

# Add the agents to the orchestrator
orchestrator.add_agent(collector)
orchestrator.add_agent(analyzer)
orchestrator.add_agent(reporter)

# Main asynchronous function
async def main():
    # Start the orchestrator
    await orchestrator.start()

    # Send a message to start the flow
    start_message = Message(
        sender_id="system",
        receiver_id="collector",
        content="Start collection",
        msg_type=MessageType.COMMAND
    )
    await orchestrator.send_message(start_message)

    # Wait for the messages to be processed
    await asyncio.sleep(2)

    # Visualize the system
    orchestrator.visualize(save_path="system_flow.png")

    # Stop the orchestrator
    await orchestrator.stop()

# Run the flow
if __name__ == "__main__":
    asyncio.run(main())
```

## 🖥️ Exporting as an API

Orchestra allows you to easily export your multi-agent system as a REST API:

```python
from orchestra import ApiExporter

# Create the orchestrator and set up agents (as in the example above)
# ...

# Export as API
api_exporter = ApiExporter(orchestrator)

# Start the server (default at http://localhost:8000)
api_exporter.run()
```

Once started, you can access the API documentation at `http://localhost:8000/docs`.

## 📊 Visualization

Orchestra provides built-in tools to visualize the flow of information:

```python
# Generate a visualization of the system
orchestrator.visualize(figsize=(12, 8), save_path="my_system.png")

# Get message flow statistics
stats = orchestrator.visualizer.get_message_flow_stats()
print(stats)
```

## 🧩 Project Structure

```
orchestra/
├── README.md                     # Main documentation
├── requirements.txt              # Project dependencies
├── setup.py                      # Installation script
├── setup_venv.sh                 # Script for Linux/Mac
├── setup_venv.bat                # Script for Windows
├── orchestra/                    # Main package
│   ├── __init__.py               # Exports main classes
│   ├── agents/                   # Agents module
│   │   ├── __init__.py
│   │   ├── base.py               # Agent interface definition
│   │   └── functional.py         # Functional agents implementation
│   ├── messaging/                # Messaging module
│   │   ├── __init__.py
│   │   └── message.py            # Message definitions
│   ├── orchestrator/             # Orchestrator module
│   │   ├── __init__.py
│   │   └── core.py               # Orchestrator implementation
│   ├── visualization/            # Visualization module
│   │   ├── __init__.py
│   │   └── visualizer.py         # Visualizer implementation
│   └── exporters/                # Exporters module
│       ├── __init__.py
│       └── api.py                # REST API exporter
└── examples/                     # Usage examples
    ├── simple_system.py          # Basic system example
    └── api_server.py             # API server example
```

## 📝 Included Examples

Orchestra includes practical examples to help you get started:

### 1. Simple System (`examples/simple_system.py`)

This example creates a basic system with three agents: coordinator, processor, and validator. It demonstrates how messages flow through the system and how agents process different types of data.

```bash
python examples/simple_system.py
```

### 2. API Server (`examples/api_server.py`)

This example shows how to export a multi-agent system as a REST API server with endpoints to manage agents and send messages.

```bash
python examples/api_server.py
```

## 💡 Use Cases

Orchestra is ideal for various scenarios:

* **Distributed Data Processing**: Split complex tasks among specialized agents.
* **Advanced Chatbot Systems**: Create chatbots with multiple "personalities" or functions.
* **Multi-Agent Simulations**: Model complex interactions between entities.
* **Automated Workflows**: Automate business processes with specialized agents.
* **Recommendation Systems**: Implement specialized components that collaborate to generate recommendations.

## 🤝 Contributing

Contributions are welcome! If you’d like to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Run the tests (`pytest`)
5. Commit your changes (`git commit -m 'Add new feature'`)
6. Push the changes to your fork (`git push origin feature/new-feature`)
7. Open a Pull Request

Please make sure to follow our [Code of Conduct](https://github.com/holasoymalva/orchestra/blob/main/CODE_OF_CONDUCT.md).

## 📄 License

This project is licensed under the [MIT License](https://github.com/holasoymalva/orchestra/blob/main/LICENSE).

## 📞 Contact

For questions, suggestions, or issues, please:

* Open an [issue](https://github.com/holasoymalva/orchestra/issues)
* Contact the maintainer: [holasoymalva](https://github.com/holasoymalva)

---

Built with ❤️ by the community. Join and contribute!
