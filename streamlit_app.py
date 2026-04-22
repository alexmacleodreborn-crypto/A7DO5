import streamlit as st
import requests
import time

API = "http://localhost:5001"

st.set_page_config(layout="wide")
st.title("🧠 A7DO Live Interface")

# Sidebar controls
st.sidebar.header("Controls")

command = st.sidebar.text_input("Command", "walk_forward")

if st.sidebar.button("Execute Command"):
    requests.post(f"{API}/api/command", json={"action": command})

if st.sidebar.button("Step Simulation"):
    requests.post(f"{API}/api/simulate/update")

# Layout
col1, col2 = st.columns(2)

# --- LEFT: Cognitive Graph ---
with col1:
    st.subheader("Cognitive Graph")

    try:
        data = requests.get(f"{API}/api/cognitive/graph").json()

        for node in data["nodes"]:
            st.write(f"🧠 {node['token']} | ⚡ {node['intensity']}")

        st.markdown("---")

        for edge in data["edges"]:
            st.write(f"{edge['from']} → {edge['to']} (R={edge['resistance']})")

    except:
        st.error("Cognitive data not available")

# --- RIGHT: System State ---
with col2:
    st.subheader("System State")

    try:
        state = requests.get(f"{API}/api/state").json()

        st.json(state)

    except:
        st.error("State not available")

# Auto refresh
time.sleep(0.5)
st.rerun()
