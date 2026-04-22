# A7DO Biomechanical Engine

A comprehensive 10-layer biomechanical simulation engine that models the human body from skeletal structure to cognitive memory.

## Overview

A7DO (Autonomous 7 Degrees of freedom Organism) is a Biomechanical Engine that simulates human anatomy and physiology across 10 integrated layers. Unlike traditional video game characters that use pre-recorded animations, A7DO uses actual biomechanical principles - muscles contract to move bones, nerves transmit signals, metabolism consumes ATP, and memory forms through Hebbian learning.

## Architecture

### Layer 01: Bones (Skeletal System)
The structural framework of A7DO. Contains 27 bones with:
- Bone IDs, names, categories (axial/appendicular)
- Articulation relationships
- Growth stage data (birth, 10 years, adulthood)
- Fracture simulation capabilities

### Layer 02: Muscles (Muscular System)
Hill-type muscle actuators that power movement. Features:
- 35 muscles with origin, insertion, action, innervation
- Real-time force calculation based on activation level
- ATP consumption and fatigue modeling
- Force-length relationships

### Layer 03: Kinematics
Forward and Inverse Kinematics engine:
- Forward Kinematics: Calculate end-effector position from joint angles
- Inverse Kinematics: Calculate joint angles to reach target positions
- FABRIK algorithm for realistic motion planning

### Layer 04: Nerves (Reflex Arcs)
The control system with 28 nerves and 6 reflex arcs:
- Cranial nerves (CN I - CN XII)
- Spinal plexuses (cervical, brachial, lumbar, sacral)
- Reflex arcs with threshold-based triggering
- Myelination simulation for improved response times

### Layer 05: Metabolic System
Energy management and fatigue modeling:
- ATP, glucose, oxygen, lactate tracking
- Heart rate and respiratory rate response
- Core temperature monitoring
- Exercise simulation with intensity and duration

### Layer 06: Sensors
Sensory input processing:
- Vision (left/right eye)
- Auditory (left/right ear)
- Vestibular (balance)
- Touch/pressure
- Pain (nociceptors)
- Temperature

### Layer 07: Blood Vessels
Cardiovascular system with 31 blood vessels:
- Arteries and veins throughout the body
- Blood perfusion calculations
- Hemorrhage simulation with compensatory responses
- Blood pressure and volume tracking

### Layer 08: Morphological Sync
Avatar synchronization for digital representation:
- Position, rotation, scale tracking
- Facial expression system
- ARKit-compatible blendshape weights
- 60 FPS sync capability

### Layer 09: Vocal Sync
Speech synthesis and lip sync:
- Text-to-phoneme conversion
- Viseme mapping for realistic lip movement
- Voice settings (pitch, speed, volume)
- Lip sync keyframe generation

### Layer 10: Cognitive Schema
The persistent associative memory system:
- Hebbian learning model
- Synaptic bridges between related concepts
- Memory decay (forgetting) simulation
- Memory consolidation (sleep) process
- Mindpathing (path of least resistance between concepts)

## Installation

```bash
cd a7do
pip install -r requirements.txt
```

## Usage

### Start the API Server

```bash
python api_server.py
```

The server will start on `http://localhost:5001`

### Python API

```python
from a7do import create_a7do

# Create A7DO instance
engine = create_a7do()

# Process cognitive input
result = engine.process_input("I remember breaking my arm")
print(f"Created node: {result['new_node']}")

# Activate a muscle
engine.layer_02_muscular.muscles['biceps_brachii'].activate(0.8)
force = engine.layer_02_muscular.muscles['biceps_brachii'].get_total_force()

# Simulate exercise
exercise_result = engine.layer_05_metabolic.simulate_exercise(0.7, 10)

# Synthesize speech
speech = engine.speak("Hello, I am A7DO.")

# Simulate injury
fracture = engine.simulate_injury(147)  # Left Femur
```

## API Endpoints

### System
- `GET /api/status` - Get system status
- `GET /api/state` - Get complete system state
- `POST /api/simulate/update` - Update simulation
- `POST /api/simulate/reset` - Reset simulation

### Layer 01: Bones
- `GET /api/bones` - Get all bones
- `GET /api/bones/<name>` - Get specific bone
- `GET /api/bones/id/<id>` - Get bone by ID
- `POST /api/simulate/fracture/<id>` - Simulate fracture

### Layer 02: Muscles
- `GET /api/muscles` - Get all muscles
- `GET /api/muscles/<name>` - Get specific muscle
- `POST /api/muscles/<name>/activate` - Activate muscle

### Layer 03: Kinematics
- `POST /api/kinematics/forward` - Forward kinematics
- `POST /api/kinematics/inverse` - Inverse kinematics

### Layer 04: Nerves
- `GET /api/nerves` - Get all nerves
- `GET /api/reflexes` - Get reflex arcs
- `POST /api/reflexes/trigger` - Trigger reflex test

### Layer 05: Metabolic
- `GET /api/organs` - Get all organs
- `GET /api/metabolic/state` - Get metabolic state
- `POST /api/simulate/exercise` - Simulate exercise

### Layer 06: Sensors
- `GET /api/sensors` - Get all sensors
- `POST /api/sensors/read` - Read sensors

### Layer 07: Cardiovascular
- `GET /api/blood-vessels` - Get all vessels
- `GET /api/cardiovascular/perfusion` - Get perfusion
- `POST /api/simulate/hemorrhage` - Simulate blood loss

### Layer 08: Avatar
- `GET /api/avatar/state` - Get avatar state
- `POST /api/avatar/expression` - Set expression
- `POST /api/avatar/position` - Set position

### Layer 09: Vocal
- `POST /api/vocal/synthesize` - Synthesize speech
- `GET/POST /api/vocal/settings` - Voice settings

### Layer 10: Cognitive
- `GET /api/cognitive/nodes` - Get cognitive nodes
- `POST /api/cognitive/nodes` - Add memory node
- `POST /api/cognitive/recall` - Recall memories
- `POST /api/cognitive/mindpath` - Find path between concepts
- `POST /api/cognitive/consolidate` - Consolidate memories

## Project Structure

```
a7do/
├── __init__.py
├── api_server.py          # Flask REST API
├── requirements.txt
├── README.md
├── core/
│   ├── __init__.py
│   └── a7do_engine.py     # Main engine implementation
├── data/
│   ├── __init__.py
│   └── anatomy_database.py # Anatomical data
└── static/
    ├── index.html         # Web interface
    ├── styles.css
    └── app.js
```

## Use Cases

### 1. Medical Simulation
Simulate injuries and observe kinematic chain impacts:
```python
fracture = engine.simulate_injury(147)  # Fracture left femur
print(fracture['kinematic_chain_impact'])
```

### 2. Exercise Physiology
Model metabolic responses to exercise:
```python
result = engine.layer_05_metabolic.simulate_exercise(0.8, 30)
print(f"Final heart rate: {result['final_state']['heart_rate']} bpm")
```

### 3. Cognitive Memory System
Build and recall associative memories:
```python
engine.layer_10_cognitive.add_node(
    token="BIRTHDAY_PARTY",
    node_class="MEMORY",
    traits=["HAPPY", "FAMILY", "CAKE"],
    intensity_voltage=8.0,
    story_context="My 10th birthday party with family"
)

recalled = engine.layer_10_cognitive.recall(["HAPPY", "FAMILY"])
```

### 4. Digital Avatar
Control a virtual representation:
```python
engine.layer_08_morphological.set_expression("happy")
speech = engine.speak("Hello, how are you today?")
```

## Data Sources

The anatomical data is based on standard medical references including:
- 27 bones across axial and appendicular skeleton
- 35 major muscles with attachment points
- 28 nerves (cranial and spinal)
- 31 blood vessels (arteries and veins)
- 24 organs across all body systems
- Growth timeline from conception to adulthood

## License

MIT License

## Author

A7DO Biomechanical Engine - Created for advanced biomechanical simulation and digital human modeling.