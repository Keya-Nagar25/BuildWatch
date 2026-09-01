"""
BuildWatch prototype - Step 3
A handful of DIFFERENT real-style failure logs to iterate your prompt against.
Swap any of these for logs you pull yourself: on GitHub, go to a repo's
Actions tab -> filter by "Failure" -> open a run -> open the failed job ->
"..." menu -> "View raw logs".

Goal for this step: run diagnose_log() on all of these and read the output
for each. If any answer is vague, wrong, or off-format, that's your signal
to edit SYSTEM_PROMPT in diagnose.py, not to add more code.
"""

LOGS = {
    "npm_peer_dependency_conflict": """
Run npm ci
npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
npm ERR! Found: react@18.2.0
npm ERR! Could not resolve dependency:
npm ERR! peer react@"^17.0.0" from react-chartjs-2@3.1.1
Error: Process completed with exit code 1.
""",

    "python_module_not_found": """
Run pytest tests/
Traceback (most recent call last):
  File "/home/runner/work/app/app/tests/test_api.py", line 3, in <module>
    import redis
ModuleNotFoundError: No module named 'redis'
==== 1 error in 0.42s ====
Error: Process completed with exit code 1.
""",

    "pytest_assertion_failure": """
Run pytest tests/
================= FAILURES =================
_____________ test_total_price _____________
    def test_total_price():
        cart = Cart(items=[Item(price=10), Item(price=5)])
>       assert cart.total() == 16
E       assert 15 == 16
E        +  where 15 = <bound method Cart.total>()
tests/test_cart.py:12: AssertionError
==== 1 failed, 4 passed in 0.88s ====
Error: Process completed with exit code 1.
""",

    "docker_build_timeout": """
Run docker build -t my-app .
Step 7/12 : RUN npm install
 ---> Running in 3f9a2b1c8d4e
npm WARN deprecated some-package@1.2.3
##[error]The operation was canceled.
##[error]The job running on runner GitHub Actions 12 has exceeded the maximum execution time of 15 minutes.
Error: Process completed with exit code 1.
""",

    "missing_env_var": """
Run node deploy.js
/home/runner/work/app/app/deploy.js:14
  throw new Error(`Missing required env var: ${key}`);
        ^
Error: Missing required env var: DATABASE_URL
    at getEnv (/home/runner/work/app/app/deploy.js:14:9)
    at Object.<anonymous> (/home/runner/work/app/app/deploy.js:22:15)
Error: Process completed with exit code 1.
""",
}
