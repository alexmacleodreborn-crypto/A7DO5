from core.state_engine import A7DOState
from core.simulation_loop import SimulationLoop
from core.command_router import CommandRouter
from core.behaviour_engine import BehaviourEngine
from core.nervous_system_patch import NervousSystemPatch
from core.engine_patch import EnginePatch

class A7DOEngine:
    def __init__(self):
        # Core state
        self.state = A7DOState()

        # Layers (your existing ones)
        self.layer_02_muscular = ...
        self.layer_03_kinematics = ...
        self.layer_04_nervous = NervousSystemPatch(self)
        self.layer_05_metabolic = ...
        self.layer_06_sensors = ...
        self.layer_07_cardiovascular = ...
        self.layer_08_morphological = ...
        self.layer_09_vocal = ...
        self.layer_10_cognitive = ...

        # Core systems
        self.behaviour = BehaviourEngine(self)
        self.command_router = CommandRouter(self)
        self.loop = SimulationLoop(self)

        # Wire everything
        self.patch = EnginePatch(self)
        self.patch.wire_layers()

    def command(self, action):
        return self.command_router.execute(action)

    def step(self, dt=0.016):
        self.loop.step(dt)
