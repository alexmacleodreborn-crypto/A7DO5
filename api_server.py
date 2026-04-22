"""
A7DO REST API Server
Flask-based API for interacting with the A7DO Biomechanical Engine
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.a7do_engine import A7DOEngine, create_a7do
from data.anatomy_database import (
    BONES, MUSCLES, NERVES, BLOOD_VESSELS, ORGANS, 
    LIGAMENTS_TENDONS, ENDOCRINE, LYMPHATIC, GROWTH_TIMELINE
)

app = Flask(__name__, static_folder='static')
CORS(app)

# Global A7DO instance
a7do: A7DOEngine = None


def get_a7do() -> A7DOEngine:
    """Get or create A7DO instance"""
    global a7do
    if a7do is None:
        a7do = create_a7do()
    return a7do


# ============================================================================
# STATIC FILES
# ============================================================================

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


# ============================================================================
# SYSTEM ENDPOINTS
# ============================================================================

@app.route('/api/status', methods=['GET'])
def get_status():
    """Get overall system status"""
    engine = get_a7do()
    return jsonify({
        "status": "operational",
        "simulation_time": engine.simulation_time,
        "layers": {
            "layer_01_skeletal": {"bones": len(engine.layer_01_skeletal.bones)},
            "layer_02_muscular": {"muscles": len(engine.layer_02_muscular.muscles)},
            "layer_03_kinematics": {"status": "ready"},
            "layer_04_nervous": {"nerves": len(engine.layer_04_nervous.nerves), "reflexes": len(engine.layer_04_nervous.reflex_arcs)},
            "layer_05_metabolic": {"organs": len(engine.layer_05_metabolic.organs)},
            "layer_06_sensors": {"sensors": len(engine.layer_06_sensors.sensors)},
            "layer_07_cardiovascular": {"vessels": len(engine.layer_07_cardiovascular.vessels)},
            "layer_08_morphological": {"status": "ready"},
            "layer_09_vocal": {"status": "ready"},
            "layer_10_cognitive": {"nodes": len(engine.layer_10_cognitive.nodes), "bridges": len(engine.layer_10_cognitive.synaptic_bridges)}
        }
    })


@app.route('/api/state', methods=['GET'])
def get_full_state():
    """Get complete system state"""
    engine = get_a7do()
    return jsonify(engine.get_full_state())


# ============================================================================
# LAYER 01: SKELETAL SYSTEM ENDPOINTS
# ============================================================================

@app.route('/api/bones', methods=['GET'])
def get_bones():
    """Get all bones"""
    return jsonify(BONES)


@app.route('/api/bones/<bone_name>', methods=['GET'])
def get_bone(bone_name):
    """Get specific bone by name"""
    engine = get_a7do()
    bone = engine.layer_01_skeletal.bones.get(bone_name)
    if bone:
        return jsonify({
            "id": bone.id,
            "name": bone.name,
            "category": bone.category,
            "articulations": bone.articulations,
            "position": bone.position,
            "rotation": bone.rotation,
            "length": bone.length,
            "mass": bone.mass
        })
    return jsonify({"error": "Bone not found"}), 404


@app.route('/api/bones/id/<int:bone_id>', methods=['GET'])
def get_bone_by_id(bone_id):
    """Get bone by ID"""
    engine = get_a7do()
    bone = engine.layer_01_skeletal.get_bone_by_id(bone_id)
    if bone:
        return jsonify({
            "id": bone.id,
            "name": bone.name,
            "category": bone.category,
            "articulations": bone.articulations,
            "length": bone.length,
            "mass": bone.mass
        })
    return jsonify({"error": "Bone not found"}), 404


@app.route('/api/simulate/fracture/<int:bone_id>', methods=['POST'])
def simulate_fracture(bone_id):
    """Simulate a bone fracture"""
    engine = get_a7do()
    result = engine.simulate_injury(bone_id, "fracture")
    return jsonify(result)


# ============================================================================
# LAYER 02: MUSCULAR SYSTEM ENDPOINTS
# ============================================================================

@app.route('/api/muscles', methods=['GET'])
def get_muscles():
    """Get all muscles"""
    return jsonify(MUSCLES)


@app.route('/api/muscles/<muscle_name>', methods=['GET'])
def get_muscle(muscle_name):
    """Get specific muscle by name"""
    engine = get_a7do()
    muscle = engine.layer_02_muscular.muscles.get(muscle_name)
    if muscle:
        return jsonify({
            "id": muscle.id,
            "name": muscle.name,
            "group": muscle.group,
            "origin": muscle.origin,
            "insertion": muscle.insertion,
            "action": muscle.action,
            "innervation": muscle.innervation,
            "activation": muscle.fibers[0].activation if muscle.fibers else 0,
            "force": muscle.get_total_force(),
            "fatigue": muscle.fatigue_factor,
            "atp_level": muscle.atp_level
        })
    return jsonify({"error": "Muscle not found"}), 404


@app.route('/api/muscles/<muscle_name>/activate', methods=['POST'])
def activate_muscle(muscle_name):
    """Activate a specific muscle"""
    engine = get_a7do()
    level = request.json.get('level', 0.5)
    
    muscle = engine.layer_02_muscular.muscles.get(muscle_name)
    if muscle:
        muscle.activate(level)
        return jsonify({
            "status": "activated",
            "muscle": muscle_name,
            "level": level,
            "force": muscle.get_total_force()
        })
    return jsonify({"error": "Muscle not found"}), 404


@app.route('/api/muscle-groups/<group_name>/activate', methods=['POST'])
def activate_muscle_group(group_name):
    """Activate all muscles in a group"""
    engine = get_a7do()
    level = request.json.get('level', 0.5)
    
    engine.layer_02_muscular.activate_muscle_group(group_name, level)
    return jsonify({
        "status": "activated",
        "group": group_name,
        "level": level
    })


# ============================================================================
# LAYER 03: KINEMATICS ENDPOINTS
# ============================================================================

@app.route('/api/kinematics/forward', methods=['POST'])
def forward_kinematics():
    """Calculate forward kinematics for a bone chain"""
    engine = get_a7do()
    chain = request.json.get('chain', [])
    
    positions = engine.layer_03_kinematics.forward_kinematics(chain)
    return jsonify({
        "chain": chain,
        "positions": positions
    })


@app.route('/api/kinematics/inverse', methods=['POST'])
def inverse_kinematics():
    """Calculate inverse kinematics to reach a target"""
    engine = get_a7do()
    chain = request.json.get('chain', [])
    target = request.json.get('target', [0.5, 0.5, 0])
    
    angles = engine.layer_03_kinematics.inverse_kinematics(
        chain, 
        tuple(target)
    )
    return jsonify({
        "chain": chain,
        "target": target,
        "joint_angles": angles
    })


# ============================================================================
# LAYER 04: NERVOUS SYSTEM ENDPOINTS
# ============================================================================

@app.route('/api/nerves', methods=['GET'])
def get_nerves():
    """Get all nerves"""
    return jsonify(NERVES)


@app.route('/api/reflexes', methods=['GET'])
def get_reflexes():
    """Get all reflex arcs"""
    engine = get_a7do()
    return jsonify([
        {
            "name": r.name,
            "sensor_type": r.sensor_type,
            "threshold": r.threshold,
            "response_muscles": r.response_muscles,
            "latency_ms": r.latency_ms,
            "myelination": r.myelination
        }
        for r in engine.layer_04_nervous.reflex_arcs
    ])


@app.route('/api/reflexes/trigger', methods=['POST'])
def trigger_reflex_check():
    """Check if a reflex should trigger based on sensory input"""
    engine = get_a7do()
    sensor_type = request.json.get('sensor_type', 'stretch')
    value = request.json.get('value', 0)
    
    responses = engine.layer_04_nervous.process_sensory_input(sensor_type, value)
    return jsonify({
        "sensor_type": sensor_type,
        "value": value,
        "reflex_responses": responses
    })


# ============================================================================
# LAYER 05: METABOLIC SYSTEM ENDPOINTS
# ============================================================================

@app.route('/api/organs', methods=['GET'])
def get_organs():
    """Get all organs"""
    return jsonify(ORGANS)


@app.route('/api/metabolic/state', methods=['GET'])
def get_metabolic_state():
    """Get current metabolic state"""
    engine = get_a7do()
    return jsonify({
        "atp_level": engine.layer_05_metabolic.state.atp_level,
        "glucose_level": engine.layer_05_metabolic.state.glucose_level,
        "oxygen_level": engine.layer_05_metabolic.state.oxygen_level,
        "lactate_level": engine.layer_05_metabolic.state.lactate_level,
        "heart_rate": engine.layer_05_metabolic.state.heart_rate,
        "respiratory_rate": engine.layer_05_metabolic.state.respiratory_rate,
        "core_temperature": engine.layer_05_metabolic.state.core_temperature,
        "fatigue_level": engine.layer_05_metabolic.get_fatigue_level()
    })


@app.route('/api/simulate/exercise', methods=['POST'])
def simulate_exercise():
    """Simulate exercise"""
    engine = get_a7do()
    intensity = request.json.get('intensity', 0.5)
    duration = request.json.get('duration_minutes', 5)
    
    result = engine.layer_05_metabolic.simulate_exercise(intensity, duration)
    return jsonify(result)


# ============================================================================
# LAYER 06: SENSORS ENDPOINTS
# ============================================================================

@app.route('/api/sensors', methods=['GET'])
def get_sensors():
    """Get all sensors"""
    engine = get_a7do()
    return jsonify({
        name: {
            "name": s.name,
            "type": s.sensor_type,
            "sensitivity": s.sensitivity,
            "range": [s.range_min, s.range_max],
            "current_value": s.current_value
        }
        for name, s in engine.layer_06_sensors.sensors.items()
    })


@app.route('/api/sensors/read', methods=['POST'])
def read_sensors():
    """Read all sensors with given inputs"""
    engine = get_a7do()
    inputs = request.json.get('inputs', {})
    readings = engine.layer_06_sensors.read_all(inputs)
    return jsonify(readings)


# ============================================================================
# LAYER 07: CARDIOVASCULAR SYSTEM ENDPOINTS
# ============================================================================

@app.route('/api/blood-vessels', methods=['GET'])
def get_blood_vessels():
    """Get all blood vessels"""
    return jsonify(BLOOD_VESSELS)


@app.route('/api/cardiovascular/perfusion', methods=['GET'])
def get_perfusion():
    """Get blood flow distribution"""
    engine = get_a7do()
    activity = request.args.get('activity', 0, type=float)
    return jsonify(engine.layer_07_cardiovascular.calculate_perfusion(activity))


@app.route('/api/simulate/hemorrhage', methods=['POST'])
def simulate_hemorrhage():
    """Simulate blood loss"""
    engine = get_a7do()
    blood_loss = request.json.get('blood_loss_liters', 0.5)
    result = engine.layer_07_cardiovascular.simulate_hemorrhage(blood_loss)
    return jsonify(result)


# ============================================================================
# LAYER 08: MORPHOLOGICAL SYNC ENDPOINTS
# ============================================================================

@app.route('/api/avatar/state', methods=['GET'])
def get_avatar_state():
    """Get current avatar state"""
    engine = get_a7do()
    return jsonify(engine.layer_08_morphological.export_avatar_state())


@app.route('/api/avatar/expression', methods=['POST'])
def set_avatar_expression():
    """Set avatar facial expression"""
    engine = get_a7do()
    expression = request.json.get('expression', 'neutral')
    engine.layer_08_morphological.set_expression(expression)
    return jsonify({
        "status": "updated",
        "expression": expression,
        "blendshapes": engine.layer_08_morphological.get_blendshape_weights()
    })


@app.route('/api/avatar/position', methods=['POST'])
def set_avatar_position():
    """Set avatar position"""
    engine = get_a7do()
    x = request.json.get('x', 0)
    y = request.json.get('y', 0)
    z = request.json.get('z', 0)
    engine.layer_08_morphological.update_position(x, y, z)
    return jsonify({"status": "updated", "position": [x, y, z]})


# ============================================================================
# LAYER 09: VOCAL SYNC ENDPOINTS
# ============================================================================

@app.route('/api/vocal/synthesize', methods=['POST'])
def synthesize_speech():
    """Synthesize speech from text"""
    engine = get_a7do()
    text = request.json.get('text', 'Hello, I am A7DO.')
    result = engine.layer_09_vocal.synthesize_speech(text)
    return jsonify(result)


@app.route('/api/vocal/settings', methods=['GET', 'POST'])
def vocal_settings():
    """Get or set voice settings"""
    engine = get_a7do()
    if request.method == 'POST':
        engine.layer_09_vocal.voice_settings.update(request.json)
        return jsonify({"status": "updated", "settings": engine.layer_09_vocal.voice_settings})
    return jsonify(engine.layer_09_vocal.voice_settings)


# ============================================================================
# LAYER 10: COGNITIVE SCHEMA ENDPOINTS
# ============================================================================

@app.route('/api/cognitive/nodes', methods=['GET'])
def get_cognitive_nodes():
    """Get all cognitive nodes"""
    engine = get_a7do()
    return jsonify(engine.layer_10_cognitive.to_json())


@app.route('/api/cognitive/nodes', methods=['POST'])
def add_cognitive_node():
    """Add a new cognitive node"""
    engine = get_a7do()
    data = request.json
    
    node = engine.layer_10_cognitive.add_node(
        token=data.get('token', f'NODE_{len(engine.layer_10_cognitive.nodes)}'),
        node_class=data.get('node_class', 'MEMORY'),
        traits=data.get('traits', []),
        intensity_voltage=data.get('intensity_voltage', 5.0),
        story_context=data.get('story_context', '')
    )
    
    return jsonify({
        "status": "created",
        "node": {
            "token": node.token,
            "class": node.node_class,
            "traits": node.traits,
            "intensity_voltage": node.intensity_voltage
        }
    })


@app.route('/api/cognitive/recall', methods=['POST'])
def recall_memories():
    """Recall memories based on traits"""
    engine = get_a7do()
    traits = request.json.get('traits', [])
    
    recalled = engine.layer_10_cognitive.recall(traits)
    return jsonify({
        "query_traits": traits,
        "results": [
            {
                "token": node.token,
                "class": node.node_class,
                "story_context": node.story_context,
                "access_strength": strength
            }
            for node, strength in recalled
        ]
    })


@app.route('/api/cognitive/mindpath', methods=['POST'])
def find_mindpath():
    """Find path between two concepts"""
    engine = get_a7do()
    start = request.json.get('start', 'BIOLOGICAL_PRIME')
    end = request.json.get('end', '')
    
    path = engine.layer_10_cognitive.mindpath(start, end)
    return jsonify({
        "start": start,
        "end": end,
        "path": path
    })


@app.route('/api/cognitive/consolidate', methods=['POST'])
def consolidate_memories():
    """Trigger memory consolidation"""
    engine = get_a7do()
    engine.layer_10_cognitive.consolidate_memories()
    return jsonify({
        "status": "consolidated",
        "total_nodes": len(engine.layer_10_cognitive.nodes),
        "total_bridges": len(engine.layer_10_cognitive.synaptic_bridges)
    })


# ============================================================================
# INPUT PROCESSING
# ============================================================================

@app.route('/api/input', methods=['POST'])
def process_input():
    """Process natural language input"""
    engine = get_a7do()
    text = request.json.get('text', '')
    
    result = engine.process_input(text)
    return jsonify(result)


# ============================================================================
# SIMULATION CONTROL
# ============================================================================

@app.route('/api/simulate/update', methods=['POST'])
def update_simulation():
    """Update simulation by time step"""
    engine = get_a7do()
    dt = request.json.get('dt', 0.1)
    inputs = request.json.get('inputs', {})
    
    engine.update(dt, inputs)
    return jsonify({
        "status": "updated",
        "simulation_time": engine.simulation_time
    })


@app.route('/api/simulate/reset', methods=['POST'])
def reset_simulation():
    """Reset simulation"""
    global a7do
    a7do = create_a7do()
    return jsonify({
        "status": "reset",
        "simulation_time": 0
    })


# ============================================================================
# DATABASE ENDPOINTS
# ============================================================================

@app.route('/api/database/growth-timeline', methods=['GET'])
def get_growth_timeline():
    """Get human growth timeline"""
    return jsonify(GROWTH_TIMELINE)


@app.route('/api/database/endocrine', methods=['GET'])
def get_endocrine():
    """Get endocrine system data"""
    return jsonify(ENDOCRINE)


@app.route('/api/database/lymphatic', methods=['GET'])
def get_lymphatic():
    """Get lymphatic system data"""
    return jsonify(LYMPHATIC)


@app.route('/api/database/ligaments-tendons', methods=['GET'])
def get_ligaments_tendons():
    """Get ligaments and tendons data"""
    return jsonify(LIGAMENTS_TENDONS)


# ============================================================================
# RUN SERVER
# ============================================================================

if __name__ == '__main__':
    print("Starting A7DO API Server...")
    print("Initializing A7DO Engine...")
    a7do = create_a7do()
    print(f"Bones: {len(a7do.layer_01_skeletal.bones)}")
    print(f"Muscles: {len(a7do.layer_02_muscular.muscles)}")
    print(f"Nerves: {len(a7do.layer_04_nervous.nerves)}")
    print(f"Blood Vessels: {len(a7do.layer_07_cardiovascular.vessels)}")
    print(f"Organs: {len(a7do.layer_05_metabolic.organs)}")
    app.run(host='0.0.0.0', port=5001, debug=True)