"""
A7DO Biomechanical Engine
Core implementation of all 10 layers of the A7DO architecture
"""

import json
import math
import time
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field, asdict
from enum import Enum
import sys
sys.path.append('..')
from data.anatomy_database import BONES, MUSCLES, NERVES, BLOOD_VESSELS, ORGANS, LIGAMENTS_TENDONS, ENDOCRINE, LYMPHATIC, GROWTH_TIMELINE


# ============================================================================
# LAYER 10: COGNITIVE SCHEMA (Associative Memory)
# ============================================================================

class NodeClass(Enum):
    CORE_IDENTITY = "CORE_IDENTITY"
    MEMORY = "MEMORY"
    PERSON = "PERSON"
    CONCEPT = "CONCEPT"
    EMOTION = "EMOTION"
    SKILL = "SKILL"
    LOCATION = "LOCATION"
    OBJECT = "OBJECT"


@dataclass
class TemporalData:
    created_at: str
    last_accessed: str
    
    def update_access(self):
        self.last_accessed = datetime.utcnow().isoformat() + "Z"


@dataclass
class CognitiveNode:
    token: str
    node_class: str
    traits: List[str]
    intensity_voltage: float
    story_context: str
    temporal_data: TemporalData
    synaptic_stability: float = 1.0
    
    def decay(self, decay_rate: float = 0.01):
        """Simulate biological forgetting through synaptic decay"""
        time_since_creation = (datetime.utcnow() - datetime.fromisoformat(self.temporal_data.created_at.replace('Z', ''))).days
        self.synaptic_stability *= math.exp(-decay_rate * time_since_creation / 365)
        if self.synaptic_stability < 0.1:
            self.synaptic_stability = 0.1
    
    def rehearse(self):
        """Strengthen memory through access"""
        self.synaptic_stability = min(1.0, self.synaptic_stability + 0.1)
        self.temporal_data.update_access()


@dataclass
class SynapticBridge:
    source_node: str
    target_node: str
    shared_traits: List[str]
    electrical_resistance_ohms: float
    status: str = "STABLE"
    
    def calculate_resistance(self, source: CognitiveNode, target: CognitiveNode):
        """Calculate resistance based on shared traits and voltage"""
        shared = len(set(source.traits) & set(target.traits))
        voltage_factor = (source.intensity_voltage + target.intensity_voltage) / 20.0
        self.electrical_resistance_ohms = max(0.01, 1.0 / (shared * voltage_factor + 0.1))


class NeocortexArray:
    """
    Layer 10: The persistent associative mind of A7DO
    Implements Hebbian learning and memory consolidation
    """
    
    def __init__(self):
        self.nodes: Dict[str, CognitiveNode] = {}
        self.synaptic_bridges: List[SynapticBridge] = []
        self._initialize_default_nodes()
    
    def _initialize_default_nodes(self):
        """Initialize with default cognitive structure"""
        # Create biological prime node
        self.add_node(
            token="BIOLOGICAL_PRIME",
            node_class=NodeClass.CORE_IDENTITY.value,
            traits=["SELF", "CREATOR", "ALIVE"],
            intensity_voltage=10.0,
            story_context="The baseline initialization of the system."
        )
    
    def add_node(self, token: str, node_class: str, traits: List[str], 
                 intensity_voltage: float, story_context: str) -> CognitiveNode:
        """Add a new cognitive node"""
        now = datetime.utcnow().isoformat() + "Z"
        node = CognitiveNode(
            token=token,
            node_class=node_class,
            traits=traits,
            intensity_voltage=intensity_voltage,
            story_context=story_context,
            temporal_data=TemporalData(created_at=now, last_accessed=now)
        )
        self.nodes[token] = node
        self._auto_bridge(node)
        return node
    
    def _auto_bridge(self, new_node: CognitiveNode):
        """Automatically create synaptic bridges based on shared traits"""
        for token, existing_node in self.nodes.items():
            if token != new_node.token:
                shared_traits = list(set(new_node.traits) & set(existing_node.traits))
                if shared_traits:
                    bridge = SynapticBridge(
                        source_node=new_node.token,
                        target_node=token,
                        shared_traits=shared_traits,
                        electrical_resistance_ohms=0.5
                    )
                    bridge.calculate_resistance(new_node, existing_node)
                    self.synaptic_bridges.append(bridge)
    
    def recall(self, query_traits: List[str]) -> List[Tuple[CognitiveNode, float]]:
        """Retrieve memories based on trait matching"""
        results = []
        for token, node in self.nodes.items():
            shared = len(set(query_traits) & set(node.traits))
            if shared > 0:
                # Factor in resistance and stability
                access_strength = shared * node.synaptic_stability * node.intensity_voltage / 10.0
                results.append((node, access_strength))
        
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:10]
    
    def mindpath(self, start_token: str, end_token: str) -> List[str]:
        """Find the path of least resistance between two concepts"""
        if start_token not in self.nodes or end_token not in self.nodes:
            return []
        
        # Simple BFS with resistance weighting
        visited = {start_token}
        queue = [(start_token, [start_token])]
        
        while queue:
            current, path = queue.pop(0)
            
            if current == end_token:
                return path
            
            # Get connected nodes
            for bridge in self.synaptic_bridges:
                next_node = None
                if bridge.source_node == current:
                    next_node = bridge.target_node
                elif bridge.target_node == current:
                    next_node = bridge.source_node
                
                if next_node and next_node not in visited and bridge.electrical_resistance_ohms < 0.8:
                    visited.add(next_node)
                    queue.append((next_node, path + [next_node]))
        
        return path
    
    def consolidate_memories(self):
        """Simulate sleep-based memory consolidation"""
        for node in self.nodes.values():
            node.decay()
        
        # Strengthen frequently accessed bridges
        for bridge in self.synaptic_bridges:
            if bridge.electrical_resistance_ohms < 0.3:
                bridge.status = "MYELINATED"
    
    def to_json(self) -> dict:
        """Export cognitive schema to JSON"""
        return {
            "neocortex_array": {
                "nodes": [
                    {
                        "token": node.token,
                        "class": node.node_class,
                        "traits": node.traits,
                        "intensity_voltage": node.intensity_voltage,
                        "story_context": node.story_context,
                        "temporal_data": asdict(node.temporal_data),
                        "synaptic_stability": node.synaptic_stability
                    }
                    for node in self.nodes.values()
                ],
                "synaptic_bridges": [asdict(bridge) for bridge in self.synaptic_bridges]
            }
        }


# ============================================================================
# LAYER 01: BONES (Skeletal System)
# ============================================================================

@dataclass
class Bone:
    id: int
    name: str
    category: str
    articulations: List[str] = field(default_factory=list)
    position: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    rotation: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    length: float = 0.0
    mass: float = 0.0
    
    def get_endpoints(self) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
        """Calculate bone endpoints based on position and rotation"""
        # Simplified - using length along Y axis
        start = self.position
        end = (
            self.position[0] + self.length * math.sin(math.radians(self.rotation[1])),
            self.position[1] + self.length * math.cos(math.radians(self.rotation[1])),
            self.position[2]
        )
        return start, end


class SkeletalSystem:
    """Layer 01: The structural framework of A7DO"""
    
    def __init__(self):
        self.bones: Dict[str, Bone] = {}
        self._load_bones()
    
    def _load_bones(self):
        """Load bones from database"""
        for key, data in BONES.items():
            bone = Bone(
                id=data.get("id", 0),
                name=data.get("name", key),
                category=data.get("category", "unknown"),
                articulations=data.get("articulations", [])
            )
            # Set growth-based dimensions
            if "growth_stages" in data:
                adult = data["growth_stages"].get("adulthood", {})
                bone.length = adult.get("length_cm", 0) / 100  # Convert to meters
                bone.mass = adult.get("weight_g", 0) / 1000  # Convert to kg
            self.bones[key] = bone
    
    def get_bone_by_id(self, bone_id: int) -> Optional[Bone]:
        """Retrieve a bone by its identifier"""
        for bone in self.bones.values():
            if bone.id == bone_id:
                return bone
        return None
    
    def get_articulations(self, bone_name: str) -> List[Bone]:
        """Get all bones connected to this bone"""
        bone = self.bones.get(bone_name)
        if not bone:
            return []
        return [self.bones.get(a) for a in bone.articulations if a in self.bones]
    
    def simulate_fracture(self, bone_id: int) -> dict:
        """Simulate the effects of a bone fracture"""
        bone = self.get_bone_by_id(bone_id)
        if not bone:
            return {"error": f"Bone ID {bone_id} not found"}
        
        return {
            "fractured_bone": bone.name,
            "kinematic_chain_impact": bone.articulations,
            "compensation_muscles": self._get_compensation_muscles(bone),
            "structural_integrity": 0.0
        }
    
    def _get_compensation_muscles(self, bone: Bone) -> List[str]:
        """Get muscles that would compensate for bone injury"""
        # Simplified logic - would be more complex in full implementation
        compensation = []
        for articulation in bone.articulations:
            compensation.extend([f"{articulation}_stabilizer_1", f"{articulation}_stabilizer_2"])
        return compensation


# ============================================================================
# LAYER 02: MUSCLES (Muscular System)
# ============================================================================

@dataclass
class MuscleFiber:
    """Represents a Hill-type muscle actuator"""
    optimal_length: float  # L0 in meters
    max_force: float  # F0 in Newtons
    current_length: float = 0.0
    activation: float = 0.0  # 0-1
    pennation_angle: float = 0.0  # degrees
    
    def calculate_force(self) -> float:
        """Hill-type muscle force calculation"""
        # Force-length relationship
        length_ratio = self.current_length / self.optimal_length
        force_length = math.exp(-((length_ratio - 1) ** 2) / 0.45)
        
        return self.max_force * self.activation * force_length * math.cos(math.radians(self.pennation_angle))


@dataclass
class Muscle:
    id: int
    name: str
    group: str
    origin: List[str] = field(default_factory=list)
    insertion: str = ""
    action: str = ""
    innervation: str = ""
    fibers: List[MuscleFiber] = field(default_factory=list)
    atp_level: float = 100.0  # Percentage
    fatigue_factor: float = 0.0
    
    def __post_init__(self):
        if not self.fibers:
            # Initialize with default fiber
            self.fibers = [MuscleFiber(optimal_length=0.1, max_force=100.0, current_length=0.1)]
    
    def activate(self, level: float):
        """Activate the muscle at given level (0-1)"""
        for fiber in self.fibers:
            fiber.activation = max(0, min(1, level))
    
    def update_fatigue(self, dt: float):
        """Update fatigue based on activation and ATP consumption"""
        if self.atp_level > 0:
            consumption = sum(f.activation for f in self.fibers) * dt * 0.01
            self.atp_level = max(0, self.atp_level - consumption)
            self.fatigue_factor = 1.0 - (self.atp_level / 100.0)
        else:
            self.fatigue_factor = 1.0
    
    def get_total_force(self) -> float:
        """Get total force output considering fatigue"""
        total = sum(f.calculate_force() for f in self.fibers)
        return total * (1.0 - self.fatigue_factor * 0.5)


class MuscularSystem:
    """Layer 02: The actuator system of A7DO"""
    
    def __init__(self):
        self.muscles: Dict[str, Muscle] = {}
        self._load_muscles()
    
    def _load_muscles(self):
        """Load muscles from database"""
        for key, data in MUSCLES.items():
            muscle = Muscle(
                id=data.get("id", 0),
                name=data.get("name", key),
                group=data.get("group", "unknown"),
                origin=data.get("origin", []) if isinstance(data.get("origin", []), list) else [data.get("origin", "")],
                insertion=data.get("insertion", ""),
                action=data.get("action", ""),
                innervation=data.get("innervation", "")
            )
            self.muscles[key] = muscle
    
    def activate_muscle_group(self, group: str, level: float):
        """Activate all muscles in a group"""
        for muscle in self.muscles.values():
            if muscle.group == group:
                muscle.activate(level)
    
    def update(self, dt: float):
        """Update all muscles (fatigue, ATP)"""
        for muscle in self.muscles.values():
            muscle.update_fatigue(dt)
    
    def get_muscle_by_action(self, action_keyword: str) -> List[Muscle]:
        """Find muscles that perform a specific action"""
        return [m for m in self.muscles.values() if action_keyword.lower() in m.action.lower()]


# ============================================================================
# LAYER 03: KINEMATICS (Forward/Inverse)
# ============================================================================

class KinematicsEngine:
    """Layer 03: Forward and Inverse Kinematics"""
    
    def __init__(self, skeleton: SkeletalSystem):
        self.skeleton = skeleton
        self.joint_angles: Dict[str, float] = {}  # In degrees
    
    def forward_kinematics(self, chain: List[str]) -> List[Tuple[float, float, float]]:
        """
        Calculate end effector position from joint angles
        Returns positions of each joint in the chain
        """
        positions = [(0.0, 0.0, 0.0)]  # Start at origin
        
        current_pos = [0.0, 0.0, 0.0]
        current_rotation = [0.0, 0.0, 0.0]
        
        for bone_name in chain:
            bone = self.skeleton.bones.get(bone_name)
            if bone:
                # Apply rotation
                angle = self.joint_angles.get(bone_name, 0.0)
                current_rotation[1] += angle
                
                # Calculate new position
                dx = bone.length * math.sin(math.radians(current_rotation[1]))
                dy = bone.length * math.cos(math.radians(current_rotation[1]))
                
                current_pos[0] += dx
                current_pos[1] += dy
                
                positions.append(tuple(current_pos))
        
        return positions
    
    def inverse_kinematics(self, chain: List[str], target: Tuple[float, float, float],
                          max_iterations: int = 100) -> Dict[str, float]:
        """
        Calculate joint angles to reach target position
        Uses FABRIK algorithm (Forward And Backward Reaching Inverse Kinematics)
        """
        positions = self.forward_kinematics(chain)
        
        if len(positions) < 2:
            return {}
        
        # Convert to list for mutability
        positions = [list(p) for p in positions]
        
        for _ in range(max_iterations):
            # Backward reaching
            positions[-1] = list(target)
            for i in range(len(positions) - 2, -1, -1):
                direction = self._normalize([
                    positions[i][0] - positions[i+1][0],
                    positions[i][1] - positions[i+1][1],
                    positions[i][2] - positions[i+1][2]
                ])
                bone = self.skeleton.bones.get(chain[min(i, len(chain)-1)])
                length = bone.length if bone else 0.1
                positions[i] = [
                    positions[i+1][0] + direction[0] * length,
                    positions[i+1][1] + direction[1] * length,
                    positions[i+1][2] + direction[2] * length
                ]
            
            # Forward reaching
            positions[0] = [0.0, 0.0, 0.0]
            for i in range(len(positions) - 1):
                direction = self._normalize([
                    positions[i+1][0] - positions[i][0],
                    positions[i+1][1] - positions[i][1],
                    positions[i+1][2] - positions[i][2]
                ])
                bone = self.skeleton.bones.get(chain[min(i, len(chain)-1)])
                length = bone.length if bone else 0.1
                positions[i+1] = [
                    positions[i][0] + direction[0] * length,
                    positions[i][1] + direction[1] * length,
                    positions[i][2] + direction[2] * length
                ]
            
            # Check convergence
            dist = math.sqrt(sum((positions[-1][i] - target[i])**2 for i in range(3)))
            if dist < 0.01:
                break
        
        # Calculate angles from positions
        angles = {}
        for i, bone_name in enumerate(chain):
            if i < len(positions) - 1:
                dx = positions[i+1][0] - positions[i][0]
                dy = positions[i+1][1] - positions[i][1]
                angles[bone_name] = math.degrees(math.atan2(dx, dy))
        
        return angles
    
    def _normalize(self, vector: List[float]) -> List[float]:
        """Normalize a vector"""
        length = math.sqrt(sum(v**2 for v in vector))
        if length == 0:
            return [0.0, 0.0, 0.0]
        return [v / length for v in vector]


# ============================================================================
# LAYER 04: NERVES (Reflex Arcs)
# ============================================================================

@dataclass
class ReflexArc:
    """Simulates a spinal reflex arc"""
    name: str
    sensor_type: str
    threshold: float
    response_muscles: List[str]
    latency_ms: float = 30.0  # Typical spinal reflex latency
    myelination: float = 1.0  # Affects conduction speed
    
    def check_trigger(self, sensor_value: float) -> bool:
        """Check if reflex should trigger"""
        return sensor_value >= self.threshold
    
    def get_response_time(self) -> float:
        """Get actual response time based on myelination"""
        return self.latency_ms / self.myelination


class NervousSystem:
    """Layer 04: The control system of A7DO"""
    
    def __init__(self):
        self.nerves: Dict[str, dict] = {}
        self.reflex_arcs: List[ReflexArc] = []
        self.brain_activity: float = 0.0
        self._load_nerves()
        self._initialize_reflexes()
    
    def _load_nerves(self):
        """Load nerves from database"""
        self.nerves = NERVES.copy()
    
    def _initialize_reflexes(self):
        """Initialize built-in reflex arcs"""
        self.reflex_arcs = [
            ReflexArc("patellar_reflex", "stretch", 5.0, ["quadriceps_femoris"], 30.0),
            ReflexArc("achilles_reflex", "stretch", 5.0, ["gastrocnemius"], 35.0),
            ReflexArc("withdrawal_reflex", "pain", 7.0, ["biceps_brachii", "triceps_brachii"], 50.0),
            ReflexArc("crossed_extensor", "pain", 7.0, ["quadriceps_femoris"], 80.0),
            ReflexArc("blink_reflex", "proximity", 0.1, ["orbicularis_oculi"], 20.0),
            ReflexArc("startle_reflex", "auditory", 80.0, ["trapezius", "sternocleidomastoid"], 40.0)
        ]
    
    def process_sensory_input(self, sensor_type: str, value: float) -> List[dict]:
        """Process sensory input and trigger reflexes"""
        responses = []
        for reflex in self.reflex_arcs:
            if reflex.sensor_type == sensor_type and reflex.check_trigger(value):
                responses.append({
                    "reflex": reflex.name,
                    "muscles": reflex.response_muscles,
                    "response_time_ms": reflex.get_response_time(),
                    "strength": min(1.0, value / reflex.threshold)
                })
        return responses
    
    def build_myelination(self, reflex_name: str, practice_count: int):
        """Improve reflex speed through practice (myelination)"""
        for reflex in self.reflex_arcs:
            if reflex.name == reflex_name:
                reflex.myelination = min(3.0, 1.0 + practice_count * 0.01)


# ============================================================================
# LAYER 05: METABOLIC SYSTEM
# ============================================================================

@dataclass
class MetabolicState:
    """Represents the metabolic state of A7DO"""
    atp_level: float = 100.0  # mmol
    glucose_level: float = 5.0  # mmol/L (blood glucose)
    oxygen_level: float = 98.0  # SpO2 percentage
    lactate_level: float = 1.0  # mmol/L
    heart_rate: int = 72  # bpm
    respiratory_rate: int = 16  # breaths/min
    core_temperature: float = 37.0  # Celsius
    
    def update(self, activity_level: float, dt: float):
        """Update metabolic state based on activity"""
        # ATP consumption and regeneration
        atp_consumption = activity_level * 0.5 * dt
        atp_regeneration = min(self.glucose_level * 0.3, self.oxygen_level * 0.01) * dt
        
        self.atp_level = max(0, min(100, self.atp_level - atp_consumption + atp_regeneration))
        
        # Glucose consumption
        self.glucose_level = max(2.0, self.glucose_level - activity_level * 0.01 * dt)
        
        # Lactate accumulation during high intensity
        if activity_level > 0.7:
            self.lactate_level = min(20.0, self.lactate_level + activity_level * 0.1 * dt)
        else:
            self.lactate_level = max(1.0, self.lactate_level - 0.05 * dt)
        
        # Heart rate response
        target_hr = 72 + int(activity_level * 108)  # Max ~180 bpm
        self.heart_rate = int(self.heart_rate + (target_hr - self.heart_rate) * 0.1)
        
        # Respiratory rate response
        target_rr = 16 + int(activity_level * 24)  # Max ~40 breaths/min
        self.respiratory_rate = int(self.respiratory_rate + (target_rr - self.respiratory_rate) * 0.1)


class MetabolicSystem:
    """Layer 05: Energy management of A7DO"""
    
    def __init__(self):
        self.state = MetabolicState()
        self.organs: Dict[str, dict] = {}
        self._load_organs()
    
    def _load_organs(self):
        """Load organs from database"""
        self.organs = ORGANS.copy()
    
    def simulate_exercise(self, intensity: float, duration_minutes: float) -> dict:
        """Simulate exercise and return metabolic changes"""
        results = []
        dt = 0.1  # Time step in minutes
        
        for t in range(int(duration_minutes / dt)):
            self.state.update(intensity, dt)
            if t % 10 == 0:
                results.append({
                    "time_minutes": t * dt,
                    "atp": self.state.atp_level,
                    "heart_rate": self.state.heart_rate,
                    "lactate": self.state.lactate_level
                })
        
        return {
            "final_state": asdict(self.state),
            "time_series": results
        }
    
    def get_fatigue_level(self) -> float:
        """Calculate overall fatigue level"""
        atp_fatigue = 1.0 - (self.state.atp_level / 100.0)
        lactate_fatigue = self.state.lactate_level / 20.0
        return (atp_fatigue + lactate_fatigue) / 2.0


# ============================================================================
# LAYER 06: SENSORS
# ============================================================================

@dataclass
class Sensor:
    name: str
    sensor_type: str
    sensitivity: float = 1.0
    range_min: float = 0.0
    range_max: float = 100.0
    current_value: float = 0.0
    
    def read(self, external_value: float) -> float:
        """Read and process sensor value"""
        clamped = max(self.range_min, min(self.range_max, external_value))
        self.current_value = clamped * self.sensitivity
        return self.current_value


class SensorSystem:
    """Layer 06: Sensory input of A7DO"""
    
    def __init__(self):
        self.sensors: Dict[str, Sensor] = {}
        self._initialize_sensors()
    
    def _initialize_sensors(self):
        """Initialize sensor array"""
        # Vision sensors
        self.sensors["left_eye"] = Sensor("left_eye", "vision", 1.0, 0, 255)
        self.sensors["right_eye"] = Sensor("right_eye", "vision", 1.0, 0, 255)
        
        # Auditory sensors
        self.sensors["left_ear"] = Sensor("left_ear", "auditory", 1.0, 0, 140)  # dB
        self.sensors["right_ear"] = Sensor("right_ear", "auditory", 1.0, 0, 140)
        
        # Proprioceptive sensors
        self.sensors["vestibular"] = Sensor("vestibular", "balance", 1.0, -90, 90)
        
        # Touch/pressure sensors
        self.sensors["skin_general"] = Sensor("skin_general", "touch", 1.0, 0, 100)
        
        # Pain sensors
        self.sensors["nociceptor"] = Sensor("nociceptor", "pain", 1.0, 0, 10)
        
        # Temperature sensors
        self.sensors["thermoreceptor"] = Sensor("thermoreceptor", "temperature", 1.0, 20, 45)
    
    def read_all(self, external_inputs: Dict[str, float]) -> Dict[str, float]:
        """Read all sensors with given external inputs"""
        return {
            name: sensor.read(external_inputs.get(name, 0))
            for name, sensor in self.sensors.items()
        }


# ============================================================================
# LAYER 07: BLOOD VESSELS
# ============================================================================

class CardiovascularSystem:
    """Layer 07: Blood circulation of A7DO"""
    
    def __init__(self):
        self.vessels: Dict[str, dict] = {}
        self.blood_volume: float = 5.0  # Liters
        self.blood_pressure_systolic: int = 120
        self.blood_pressure_diastolic: int = 80
        self._load_vessels()
    
    def _load_vessels(self):
        """Load blood vessels from database"""
        self.vessels = BLOOD_VESSELS.copy()
    
    def calculate_perfusion(self, activity_level: float) -> dict:
        """Calculate blood flow distribution"""
        # Resting cardiac output ~5 L/min, can increase to 20+ L/min during exercise
        cardiac_output = 5.0 * (1 + activity_level * 3)
        
        return {
            "cardiac_output_L_min": cardiac_output,
            "brain_perfusion": cardiac_output * 0.15,
            "heart_perfusion": cardiac_output * 0.05,
            "muscle_perfusion": cardiac_output * (0.2 + activity_level * 0.5),
            "organ_perfusion": cardiac_output * (0.4 - activity_level * 0.2),
            "skin_perfusion": cardiac_output * (0.1 + activity_level * 0.1)
        }
    
    def simulate_hemorrhage(self, blood_loss_liters: float) -> dict:
        """Simulate blood loss and compensatory responses"""
        self.blood_volume -= blood_loss_liters
        loss_percentage = blood_loss_liters / 5.0
        
        # Compensatory responses
        if loss_percentage < 0.15:
            # Class I hemorrhage - minimal changes
            return {"status": "stable", "hr_change": 0, "bp_change": 0}
        elif loss_percentage < 0.30:
            # Class II - tachycardia
            return {"status": "compensated", "hr_change": 20, "bp_change": -10}
        elif loss_percentage < 0.40:
            # Class III - significant shock
            return {"status": "decompensating", "hr_change": 40, "bp_change": -30}
        else:
            # Class IV - severe shock
            return {"status": "critical", "hr_change": 60, "bp_change": -50}


# ============================================================================
# LAYER 08: MORPHOLOGICAL SYNC
# ============================================================================

class MorphologicalSync:
    """Layer 08: Avatar synchronization"""
    
    def __init__(self):
        self.avatar_state = {
            "position": (0.0, 0.0, 0.0),
            "rotation": (0.0, 0.0, 0.0),
            "scale": 1.0,
            "expression": "neutral",
            "gesture": "idle"
        }
        self.sync_latency_ms: float = 16.67  # ~60 FPS
    
    def update_position(self, x: float, y: float, z: float):
        """Update avatar position"""
        self.avatar_state["position"] = (x, y, z)
    
    def update_rotation(self, pitch: float, yaw: float, roll: float):
        """Update avatar rotation"""
        self.avatar_state["rotation"] = (pitch, yaw, roll)
    
    def set_expression(self, expression: str):
        """Set facial expression"""
        valid_expressions = ["neutral", "happy", "sad", "angry", "surprised", "fear", "disgust"]
        if expression in valid_expressions:
            self.avatar_state["expression"] = expression
    
    def get_blendshape_weights(self) -> Dict[str, float]:
        """Get ARKit-compatible blendshape weights"""
        expression = self.avatar_state["expression"]
        
        weights = {
            "neutral": {"eyeBlinkLeft": 0, "eyeBlinkRight": 0, "jawOpen": 0, "mouthSmile": 0},
            "happy": {"eyeBlinkLeft": 0.3, "eyeBlinkRight": 0.3, "jawOpen": 0.1, "mouthSmile": 1.0},
            "sad": {"eyeBlinkLeft": 0.5, "eyeBlinkRight": 0.5, "browDownLeft": 0.7, "browDownRight": 0.7},
            "angry": {"browDownLeft": 1.0, "browDownRight": 1.0, "jawForward": 0.3},
            "surprised": {"eyeWideLeft": 1.0, "eyeWideRight": 1.0, "jawOpen": 0.5, "browUpLeft": 1.0, "browUpRight": 1.0}
        }
        
        return weights.get(expression, weights["neutral"])
    
    def export_avatar_state(self) -> dict:
        """Export current avatar state for rendering"""
        return {
            "transform": {
                "position": self.avatar_state["position"],
                "rotation": self.avatar_state["rotation"],
                "scale": self.avatar_state["scale"]
            },
            "expression": self.avatar_state["expression"],
            "blendshapes": self.get_blendshape_weights(),
            "gesture": self.avatar_state["gesture"]
        }


# ============================================================================
# LAYER 09: VOCAL SYNC
# ============================================================================

class VocalSync:
    """Layer 09: Voice synthesis and lip sync"""
    
    def __init__(self):
        self.voice_settings = {
            "pitch": 1.0,  # 0.5-2.0
            "speed": 1.0,  # 0.5-2.0
            "volume": 1.0  # 0.0-1.0
        }
        self.phoneme_queue: List[str] = []
    
    def text_to_phonemes(self, text: str) -> List[str]:
        """Convert text to phoneme sequence (simplified)"""
        # Simplified phoneme mapping
        phoneme_map = {
            'a': 'AE', 'e': 'EH', 'i': 'IY', 'o': 'OW', 'u': 'UW',
            'b': 'B', 'c': 'K', 'd': 'D', 'f': 'F', 'g': 'G',
            'h': 'HH', 'j': 'JH', 'k': 'K', 'l': 'L', 'm': 'M',
            'n': 'N', 'p': 'P', 'q': 'K', 'r': 'R', 's': 'S',
            't': 'T', 'v': 'V', 'w': 'W', 'x': 'K', 'y': 'Y', 'z': 'Z'
        }
        
        phonemes = []
        for char in text.lower():
            if char in phoneme_map:
                phonemes.append(phoneme_map[char])
            elif char == ' ':
                phonemes.append('SIL')
        
        return phonemes
    
    def phoneme_to_viseme(self, phoneme: str) -> str:
        """Map phoneme to viseme for lip sync"""
        viseme_map = {
            'AE': 'A', 'AH': 'A', 'AA': 'A',
            'EH': 'E', 'IH': 'E', 'IY': 'E',
            'OW': 'O', 'UW': 'U',
            'B': 'M', 'M': 'M', 'P': 'M',
            'F': 'F', 'V': 'F',
            'TH': 'TH', 'DH': 'TH',
            'L': 'L', 'R': 'R',
            'S': 'S', 'Z': 'S',
            'SIL': 'X'
        }
        return viseme_map.get(phoneme, 'X')
    
    def get_lip_sync_data(self, text: str, duration_ms: float) -> List[dict]:
        """Generate lip sync keyframes"""
        phonemes = self.text_to_phonemes(text)
        phoneme_duration = duration_ms / max(len(phonemes), 1)
        
        keyframes = []
        current_time = 0
        
        for phoneme in phonemes:
            viseme = self.phoneme_to_viseme(phoneme)
            keyframes.append({
                "time_ms": current_time,
                "viseme": viseme,
                "intensity": 1.0
            })
            current_time += phoneme_duration
        
        return keyframes
    
    def synthesize_speech(self, text: str) -> dict:
        """Generate speech synthesis parameters"""
        phonemes = self.text_to_phonemes(text)
        duration = len(text) * 60 / self.voice_settings["speed"]  # ~60ms per character
        
        return {
            "text": text,
            "phonemes": phonemes,
            "duration_ms": duration,
            "lip_sync": self.get_lip_sync_data(text, duration),
            "voice_settings": self.voice_settings.copy()
        }


# ============================================================================
# A7DO MAIN ENGINE
# ============================================================================

class A7DOEngine:
    """
    The complete A7DO Biomechanical Engine
    Integrates all 10 layers into a unified system
    """
    
    def __init__(self):
        # Initialize all layers
        self.layer_10_cognitive = NeocortexArray()
        self.layer_01_skeletal = SkeletalSystem()
        self.layer_02_muscular = MuscularSystem()
        self.layer_03_kinematics = KinematicsEngine(self.layer_01_skeletal)
        self.layer_04_nervous = NervousSystem()
        self.layer_05_metabolic = MetabolicSystem()
        self.layer_06_sensors = SensorSystem()
        self.layer_07_cardiovascular = CardiovascularSystem()
        self.layer_08_morphological = MorphologicalSync()
        self.layer_09_vocal = VocalSync()
        
        self.simulation_time: float = 0.0
        self.is_running: bool = False
    
    def update(self, dt: float, external_inputs: Optional[Dict] = None):
        """Update all systems by time step dt (seconds)"""
        self.simulation_time += dt
        
        # Process sensory input
        if external_inputs:
            sensor_readings = self.layer_06_sensors.read_all(external_inputs)
            
            # Process reflexes
            for sensor_type, value in sensor_readings.items():
                reflexes = self.layer_04_nervous.process_sensory_input(sensor_type, value)
                for reflex in reflexes:
                    self.layer_02_muscular.activate_muscle_group(
                        reflex["muscles"][0] if reflex["muscles"] else "unknown",
                        reflex["strength"]
                    )
        
        # Update muscular system
        self.layer_02_muscular.update(dt)
        
        # Update metabolic system
        activity = sum(m.get_total_force() for m in self.layer_02_muscular.muscles.values()) / 10000.0
        self.layer_05_metabolic.state.update(activity, dt / 60.0)
    
    def get_full_state(self) -> dict:
        """Get complete system state"""
        return {
            "simulation_time": self.simulation_time,
            "cognitive": self.layer_10_cognitive.to_json(),
            "skeletal": {
                name: {"id": b.id, "name": b.name, "length": b.length}
                for name, b in self.layer_01_skeletal.bones.items()
            },
            "muscular": {
                name: {
                    "id": m.id,
                    "name": m.name,
                    "activation": m.fibers[0].activation if m.fibers else 0,
                    "force": m.get_total_force(),
                    "fatigue": m.fatigue_factor
                }
                for name, m in self.layer_02_muscular.muscles.items()
            },
            "metabolic": asdict(self.layer_05_metabolic.state),
            "avatar": self.layer_08_morphological.export_avatar_state(),
            "cardiovascular": {
                "blood_volume": self.layer_07_cardiovascular.blood_volume,
                "blood_pressure": f"{self.layer_07_cardiovascular.blood_pressure_systolic}/{self.layer_07_cardiovascular.blood_pressure_diastolic}"
            }
        }
    
    def process_input(self, text: str) -> dict:
        """Process natural language input through cognitive layer"""
        # Extract traits from input (simplified NLP)
        traits = text.lower().split()
        
        # Recall related memories
        recalled = self.layer_10_cognitive.recall(traits)
        
        # Create new memory node
        self.layer_10_cognitive.add_node(
            token=f"INPUT_{int(self.simulation_time)}",
            node_class="MEMORY",
            traits=traits,
            intensity_voltage=5.0,
            story_context=text
        )
        
        return {
            "recalled_memories": [(n.token, score) for n, score in recalled],
            "new_node": f"INPUT_{int(self.simulation_time)}",
            "total_nodes": len(self.layer_10_cognitive.nodes)
        }
    
    def simulate_injury(self, bone_id: int, injury_type: str = "fracture") -> dict:
        """Simulate an injury and its effects"""
        fracture_result = self.layer_01_skeletal.simulate_fracture(bone_id)
        
        # Add trauma memory
        bone = self.layer_01_skeletal.get_bone_by_id(bone_id)
        if bone:
            self.layer_10_cognitive.add_node(
                token=f"TRAUMA_{bone.name.upper()}",
                node_class="MEMORY",
                traits=["PAIN", "TRAUMA", "INJURY", bone.name.upper()],
                intensity_voltage=9.0,
                story_context=f"Sustained {injury_type} to {bone.name}"
            )
        
        return fracture_result
    
    def speak(self, text: str) -> dict:
        """Generate speech output"""
        return self.layer_09_vocal.synthesize_speech(text)
    
    def to_json(self) -> dict:
        """Export entire engine state as JSON"""
        return self.get_full_state()


# Create default instance
def create_a7do() -> A7DOEngine:
    """Factory function to create A7DO instance"""
    return A7DOEngine()


if __name__ == "__main__":
    # Demo
    engine = create_a7do()
    print("A7DO Engine initialized")
    print(f"Bones loaded: {len(engine.layer_01_skeletal.bones)}")
    print(f"Muscles loaded: {len(engine.layer_02_muscular.muscles)}")
    print(f"Nerves loaded: {len(engine.layer_04_nervous.nerves)}")
    print(f"Blood vessels loaded: {len(engine.layer_07_cardiovascular.vessels)}")
    print(f"Organs loaded: {len(engine.layer_05_metabolic.organs)}")