# AgentOps-CLI

A modular, lightweight command-line AI agent built in Python for automating system operations and developer workflows with human-in-the-loop safety gates.

## Features
- **ReAct Execution Cycle:** Plans shell commands from natural language goals and executes them via subprocess sandboxes.
- **Safety Interceptor:** Blocks hazardous system-level operations and requires manual user confirmation before running.
- **Automated Self-Correction:** Captures non-zero return codes and stderr tracebacks, feeding them back into the model to propose fixed commands.
- **Multi-Turn Context:** Handles iterative debugging and task execution in a clean terminal interface.

## Tech Stack
- **Language:** Python
- **LLM Engine:** Google Gemini API (`gemini-2.5-flash`)
- **CLI & Formatting:** Rich
- **Execution:** Python Subprocess Sandbox

## Quickstart

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/agentops-cli.git](https://github.com/your-username/agentops-cli.git)
cd agentops-cli