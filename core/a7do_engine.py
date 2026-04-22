from core.state_engine import A7DOState
from core.simulation_loop import SimulationLoop
from core.command_router import CommandRouter
from core.behaviour_engine import BehaviourEngine
from core.nervous_system_patch import NervousSystemPatch


# -------------------------
# SIMPLE MUSCLE MODEL
# -------------------------
class Muscle:
    def __init__(self, name):
        self.name = name
        self.activation = 0.0

    def activate(self, value):
        self.activation = max(0.0, min(1.0, value))


class MuscularSystem:
    def __init__(self):
        self.muscles = {
            "biceps_brachii": Muscle("biceps_brachii"),
            "deltoid": Muscle("deltoid"),
            "quadriceps": Muscle("quadriceps"),
            "hamstrings": Muscle("hamstrings"),
            "calves": Muscle("calves"),
        }

    def apply_signals(self, signals):
        for m, a in signals.items():
            if m in self.muscles:
                self.muscles[m].activate(a)


# -------------------------
# SIMPLE COGNITIVE MODEL
# -------------------------
class CognitiveNode:
    def __init__(self, token, traits, intensity):
        self.token = token
        self.traits = traits
        self.intensity_voltage = intensity


class CognitiveSystem:
    def __init__(self):
        self.nodes = {}
        self.connections = []

    def add_node(self, token, node_class="MEMORY", traits=None, intensity_voltage=1.0, story_context=""):
        node_id = str(len(self.nodes) + 1)
        self.nodes[node_id] = CognitiveNode(token, traits or [], intensity_voltage)
        return node_id

    def recall(self, traits):
        results = []
        for node in self.nodes.values():
            if any(t in node.traits for t in traits):
                results.append(node.token)
        return results

    def process(self, state):
        # very basic decision system
        return ["walk_forward"]

    def learn(self, state):
        pass

    def consolidate(self):
        pass


# -------------------------
# ENGINE
# -------------------------
class A7DOEngine:
    def __init__(self):
        self.state = A7DOState()

        # Layers
        self.layer_02_muscular = MuscularSystem()
        self.layer_04_nervous = NervousSystemPatch(self)
        self.layer_10_cognitive = CognitiveSystem()

        # Core systems
        self.behaviour = BehaviourEngine(self)
        self.command_router = CommandRouter(self)
        self.loop = SimulationLoop(self)

    def command(self, action):
        return self.command_router.execute(action)

    def step(self, dt=0.016):
        self.loop.step(dt)
