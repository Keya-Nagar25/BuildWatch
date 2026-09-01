"""
BuildWatch prototype - Step 4
Streamlit wrapper: paste a log, click a button, see the diagnosis.
This is what you record for the demo video.

Run:
    pip install streamlit
    streamlit run app.py
"""

import streamlit as st
from diagnose import diagnose_log
from sample_logs import LOGS

st.set_page_config(page_title="BuildWatch", page_icon="🛠️")

st.title("🛠️ BuildWatch")
st.caption("Paste a failed build/CI log below and get an instant, offline diagnosis.")

# Optional convenience: let the demo pick a pre-loaded sample log instead of
# typing/pasting live, so you always have a reliable fallback mid-recording.
preset = st.selectbox(
    "Load a sample log (optional)",
    ["-- paste your own below --"] + list(LOGS.keys()),
)

default_text = LOGS[preset] if preset in LOGS else ""
log_input = st.text_area("Build failure log", value=default_text.strip(), height=250)

if st.button("Diagnose", type="primary"):
    if not log_input.strip():
        st.warning("Paste a log first.")
    else:
        with st.spinner("Running on-device model..."):
            result = diagnose_log(log_input)
        st.success("Diagnosis ready")
        st.markdown(f"```\n{result}\n```")
