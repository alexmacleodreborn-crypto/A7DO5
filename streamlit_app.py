import streamlit as st
import time

# Import engine directly
from core.a7do_engine import A7DOEngine

st.set_page_config(layout="wide")

# =========================
# INIT ENGINE (PERSISTENT)
# =========================
if "engine" not in st.session_state:
    st.session_state.engine = A7DOEngine()

engine = st.session_state.engine

# =========================
# TITLE
# =========================
st.title("🧠 A7DO Live System (Standalone)")

# =========================
# SIDEBAR CONTROLS
# =========================
st.sidebar.header("Controls")

command = st.sidebar.text_input("Command", "walk_forward")

if st.sidebar.button("Execute Command"):
    engine.command(command)

if st.sidebar.button("Step Simulation"):
    engine.step(0.016)

if st.sidebar.button("Run Continuous"):
    st.session_state.running = True

if st.sidebar.button("Stop"):
    st.session_state.running = False

# =========================
# CONTINUOUS LOOP
# =========================
if "running" not in st.session_state:
    st.session_state.running = False

if st.session_state.running:
    engine.step(0.016)
    time.sleep(0.05)
    st.rerun()

# =========================
# LAYOUT
# =========================
col1, col2 = st.columns(2)

# =========================
# COGNITIVE VIEW
# =========================
with col1:
    st.subheader("🧠 Cognitive System")

    nodes = engine.layer_10_cognitive.nodes
    connections = engine.layer_10_cognitive.connections

    for node_id, node in nodes.items():
        st.write(
            f"{node.token} | ⚡ {getattr(node, 'intensity_voltage', 1.0)}"
        )

    st.markdown("---")

    for conn in connections:
        st.write(
            f"{conn.get('from')} → {conn.get('to')} (R={conn.get('resistance',1.0)})"
        )

# =========================
# SYSTEM STATE
# =========================
with col2:
    st.subheader("⚙️ System State")

    st.json({
        "time": engine.state.time,
        "metabolic": engine.state.metabolic,
        "sensory": engine.state.sensory,
        "cognitive": engine.state.cognitive
    })

# =========================
# QUICK ACTIONS
# =========================
st.markdown("---")
st.subheader("Quick Actions")

colA, colB, colC = st.columns(3)

with colA:
    if st.button("Add Memory"):
        engine.layer_10_cognitive.add_node(
            token="BROKEN_ARM",
            node_class="MEMORY",
            traits=["PAIN", "INJURY"],
            intensity_voltage=9.0,
            story_context="Simulated injury"
        )

with colB:
    if st.button("Recall PAIN"):
        result = engine.layer_10_cognitive.recall(["PAIN"])
        st.write(result)

with colC:
    if st.button("Consolidate"):
        engine.layer_10_cognitive.consolidate()
