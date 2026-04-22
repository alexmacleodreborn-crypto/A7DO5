class NervousSystemPatch:
    def __init__(self, engine):
        self.engine = engine

    def transmit(self, commands):
        # Simulate signal delay and strength
        signals = {}
        fatigue = self.engine.state.metabolic.get("fatigue", 0)

        for muscle, activation in commands.items():
            signal_strength = activation * (1 - fatigue)
            delay = 0.01 + fatigue * 0.05

            signals[muscle] = max(0, signal_strength)

        return signals
