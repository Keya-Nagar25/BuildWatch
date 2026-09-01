"""
BuildWatch prototype - Step 3 (runner)
Runs diagnose_log() against every log in sample_logs.py so you can eyeball
the model's output across different failure types in one go.

Run:
    python test_prompt.py
"""

from diagnose import diagnose_log
from sample_logs import LOGS

for name, log_text in LOGS.items():
    print(f"\n{'=' * 60}")
    print(f"LOG: {name}")
    print("=" * 60)
    result = diagnose_log(log_text)
    print(result)
