"""
BuildWatch prototype - Step 1-2
Reads a build failure log, sends it to a local Ollama model, prints the diagnosis.

Run:
    ollama pull phi3:mini      (only needed once)
    pip install requests
    python diagnose.py
"""

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3:mini"  

SYSTEM_PROMPT = """You are BuildWatch, a CI/CD build failure triage assistant.
You will be given the raw log output of a failed build or CI job.

Respond in EXACTLY this format, nothing else, no extra commentary:

Failure type: <one short phrase, e.g. "dependency conflict", "syntax error", "test failure", "timeout", "missing environment variable">
Root cause: <one or two sentences explaining what in the log actually caused the failure>
Suggested fix: <one or two concrete, actionable sentences telling the developer exactly what to do next>

Rules:
- Base your answer only on evidence in the log. Do not invent file names or line numbers that are not present.
- If the log is ambiguous or truncated, say so honestly in "Root cause" rather than guessing confidently.
- Keep each line short enough to read at a glance on a phone screen.
"""

SAMPLE_LOG = """
Run npm ci
npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
npm ERR!
npm ERR! While resolving: my-app@1.0.0
npm ERR! Found: react@18.2.0
npm ERR! node_modules/react
npm ERR!   react@"^18.2.0" from the root project
npm ERR!
npm ERR! Could not resolve dependency:
npm ERR! peer react@"^17.0.0" from react-chartjs-2@3.1.1
npm ERR! node_modules/react-chartjs-2
npm ERR!   react-chartjs-2@"^3.1.1" from the root project
npm ERR!
npm ERR! Fix the upstream dependency conflict, or retry
npm ERR! this command with --force or --legacy-peer-deps
npm ERR! to accept an incorrect (and potentially broken) dependency resolution.
Error: Process completed with exit code 1.
"""


def diagnose_log(log_text: str) -> str:
    """Send a log to the local Ollama model and return its diagnosis text."""
    payload = {
        "model": MODEL,
        "prompt": f"{SYSTEM_PROMPT}\n\nLOG:\n{log_text}\n\nYour response:",
        "stream": False,
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()
    return response.json()["response"].strip()


if __name__ == "__main__":
    print("Sending log to Ollama, please wait...\n")
    result = diagnose_log(SAMPLE_LOG)
    print("=== BuildWatch Diagnosis ===")
    print(result)
