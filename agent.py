import os
from google import genai
from rich.console import Console
from tools import execute_shell_command

console = Console()
client = genai.Client()

SYSTEM_PROMPT = """
You are an automated CLI assistant running on Windows Command Prompt/PowerShell. 
When given a task, respond ONLY with the exact shell command to solve it.
Do not wrap the command in markdown backticks or explanations. 
If the user supplies an error message, output the corrected command to resolve it.
"""

def main():
    console.print("[bold green]AgentOps CLI Initialized.[/bold green] Type 'exit' to quit.\n")
    
    while True:
        task = console.input("[bold blue]Task > [/bold blue]")
        if task.lower() in ["exit", "quit"]:
            break

        # Step 1: Query Gemini 3.8 Flash
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"{SYSTEM_PROMPT}\nUser task: {task}"
        )
        command = response.text.strip().replace("`", "")

        console.print(f"[yellow]Proposed Command:[/yellow] [bold]{command}[/bold]")
        
        confirm = console.input("[bold red]Execute command? (y/n): [/bold red]")
        if confirm.lower() != "y":
            console.print("[dim]Aborted by user.[/dim]\n")
            continue

        result = execute_shell_command(command)
        if result["success"]:
            console.print(f"[green]Success:[/green]\n{result['output']}\n")
        else:
            console.print(f"[red]Error detected:[/red] {result['output']}")
            console.print("[yellow]Attempting self-healing with LLM...[/yellow]")
            
            # Step 2: Self-healing with Gemini 3.8 Flash
            fix_response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=f"{SYSTEM_PROMPT}\nCommand '{command}' failed with error: {result['output']}. Provide corrected command."
            )
            fixed_cmd = fix_response.text.strip().replace("`", "")
            console.print(f"[yellow]Corrected Command:[/yellow] [bold]{fixed_cmd}[/bold]\n")

if __name__ == "__main__":
    main()