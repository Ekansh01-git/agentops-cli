# AgentOps-CLI
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Model: Gemini](https://img.shields.io/badge/LLM-Gemini--3.8--Flash-orange.svg)](https://ai.google.dev/)
[![CLI: Rich](https://img.shields.io/badge/CLI-Rich-purple.svg)](https://github.com/Textualize/rich)

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

## Example Terminal Run

```text
AgentOps CLI Initialized. Type 'exit' to quit.

Task > check free disk space on drive C
Proposed Command: wmic logicaldisk get caption,freespace
Execute command? (y/n): y
Success:
Caption  FreeSpace
C:       84293021696

Task > show process list using brokenproc123
Proposed Command: brokenproc123
Execute command? (y/n): y
Error detected: 'brokenproc123' is not recognized as an internal or external command...
Attempting self-healing with LLM...
Corrected Command: tasklist
```

## Quickstart

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/agentops-cli.git](https://github.com/your-username/agentops-cli.git)
cd agentops-cli