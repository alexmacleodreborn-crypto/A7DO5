from flask import Flask, jsonify, request
from flask_cors import CORS

# Import your engine
from core.a7do_engine import A7DOEngine

app = Flask(__name__)
CORS(app)

# =========================
# INIT ENGINE
# =========================
engine = A7DOEngine()

# =========================
# SYSTEM ENDPOINTS
# =========================

@app.route("/api/status")
def status():
    return jsonify({
        "status": "running",
        "time": engine.state.time
    })


@app.route("/api/state")
def get_state():
    return jsonify({
        "time": engine.state.time,
        "metabolic": engine.state.metabolic,
        "sensory": engine.state.sensory,
        "cognitive": engine.state.cognitive
    })


@app.route("/api/simulate/update", methods=["POST"])
def simulate_update():
    dt = request.json.get("dt", 0.016) if request.json else 0.016
    engine.step(dt)
    return jsonify({"status": "step complete", "time": engine.state.time})


@app.route("/api/simulate/reset", methods=["POST"])
def reset():
    global engine
    engine = A7DOEngine()
    return jsonify({"status": "reset complete"})


# =========================
# COMMAND SYSTEM
# =========================

@app.route("/api/command", methods=["POST"])
def command():
    data = request.json
    action = data.get("action")

    result = engine.command(action)

    return jsonify({
        "action": action,
        "result": result
    })


# =========================
# COGNITIVE SYSTEM
# =========================

@app.route("/api/cognitive/nodes")
def get_nodes():
    nodes = []

    for node_id, node in engine.layer_10_cognitive.nodes.items():
        nodes.append({
            "id": node_id,
            "token": getattr(node, "token", str(node_id)),
            "traits": getattr(node, "traits", []),
            "intensity": getattr(node, "intensity_voltage", 1.0)
        })

    return jsonify(nodes)


@app.route("/api/cognitive/nodes", methods=["POST"])
def add_node():
    data = request.json

    node = engine.layer_10_cognitive.add_node(
        token=data.get("token"),
        node_class=data.get("node_class", "MEMORY"),
        traits=data.get("traits", []),
        intensity_voltage=data.get("intensity_voltage", 1.0),
        story_context=data.get("story_context", "")
    )

    return jsonify({"created": node})


@app.route("/api/cognitive/recall", methods=["POST"])
def recall():
    data = request.json
    traits = data.get("traits", [])

    result = engine.layer_10_cognitive.recall(traits)

    return jsonify(result)


@app.route("/api/cognitive/mindpath", methods=["POST"])
def mindpath():
    data = request.json

    start = data.get("from")
    end = data.get("to")

    path = engine.layer_10_cognitive.find_path(start, end)

    return jsonify({
        "from": start,
        "to": end,
        "path": path
    })


@app.route("/api/cognitive/consolidate", methods=["POST"])
def consolidate():
    engine.layer_10_cognitive.consolidate()

    return jsonify({"status": "consolidated"})


# =========================
# COGNITIVE GRAPH (FOR UI)
# =========================

@app.route("/api/cognitive/graph")
def cognitive_graph():
    nodes = []
    edges = []

    # Nodes
    for node_id, node in engine.layer_10_cognitive.nodes.items():
        nodes.append({
            "id": node_id,
            "token": getattr(node, "token", str(node_id)),
            "intensity": getattr(node, "intensity_voltage", 1.0)
        })

    # Connections
    for conn in engine.layer_10_cognitive.connections:
        edges.append({
            "from": conn.get("from"),
            "to": conn.get("to"),
            "resistance": conn.get("resistance", 1.0)
        })

    return jsonify({
        "nodes": nodes,
        "edges": edges
    })


# =========================
# METABOLIC SYSTEM
# =========================

@app.route("/api/metabolic/state")
def metabolic_state():
    return jsonify(engine.state.metabolic)


@app.route("/api/simulate/exercise", methods=["POST"])
def exercise():
    data = request.json

    intensity = data.get("intensity", 0.5)
    duration = data.get("duration", 10)

    result = engine.layer_05_metabolic.simulate_exercise(intensity, duration)

    return jsonify(result)


# =========================
# SENSORS
# =========================

@app.route("/api/sensors")
def sensors():
    return jsonify(engine.layer_06_sensors.read_all())


# =========================
# CARDIOVASCULAR
# =========================

@app.route("/api/cardiovascular/perfusion")
def perfusion():
    return jsonify(engine.layer_07_cardiovascular.get_perfusion())


# =========================
# AVATAR
# =========================

@app.route("/api/avatar/state")
def avatar_state():
    return jsonify(engine.state.avatar)


@app.route("/api/avatar/expression", methods=["POST"])
def avatar_expression():
    data = request.json
    expression = data.get("expression")

    engine.layer_08_morphological.set_expression(expression)

    return jsonify({"expression": expression})


# =========================
# VOCAL
# =========================

@app.route("/api/vocal/synthesize", methods=["POST"])
def vocal():
    data = request.json
    text = data.get("text", "")

    result = engine.layer_09_vocal.synthesize(text)

    return jsonify(result)


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
