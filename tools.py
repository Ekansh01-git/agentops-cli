import subprocess

def execute_shell_command(command: str) -> dict:
    """Executes a system shell command safely and captures output or errors."""
    # Safety filter: prevent dangerous disk wipe operations
    blocked_keywords = ["rmdir /s /q c:\\", "format ", "del /f /s /q c:\\"]
    if any(blocked in command.lower() for blocked in blocked_keywords):
        return {"success": False, "output": "Blocked: Unsafe command detected."}

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return {"success": True, "output": result.stdout.strip()}
        else:
            return {"success": False, "output": result.stderr.strip()}
    except Exception as e:
        return {"success": False, "output": str(e)}







