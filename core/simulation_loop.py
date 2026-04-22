import time

class SimulationLoop:
    def __init__(self, engine):
        self.engine = engine
        self.running = False

    def step(self, dt=0.016):
        state = self.engine.state

        # 1. Sensors
        state.sensory = self.engine.layer_06_sensors.read_all()

        # 2. Cognitive
        decisions = self.engine.layer_10_cognitive.process(state)

        # 3. Behaviour
        commands = self.engine.behaviour.generate(decisions)

        # 4. Nervous system
        signals = self.engine.layer_04_nervous.transmit(commands)

        # 5. Muscles
        self.engine.layer_02_muscular.apply_signals(signals)

        # 6. Kinematics
        self.engine.layer_03_kinematics.update(state)

        # 7. Metabolism
        self.engine.layer_05_metabolic.consume(state)

        # 8. Cardiovascular
        self.engine.layer_07_cardiovascular.update(state)

        # 9. Learning
        self.engine.layer_10_cognitive.learn(state)

        # 10. Output
        self.engine.layer_08_morphological.sync(state)
        self.engine.layer_09_vocal.sync(state)

        state.update_time(dt)

    def run(self, dt=0.016):
        self.running = True
        while self.running:
            self.step(dt)
            time.sleep(dt)

    def stop(self):
        self.running = False
