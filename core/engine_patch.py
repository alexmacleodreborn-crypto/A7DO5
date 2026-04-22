class EnginePatch:
    def __init__(self, engine):
        self.engine = engine

    def wire_layers(self):
        # Attach state references
        for layer_name in dir(self.engine):
            if layer_name.startswith("layer_"):
                layer = getattr(self.engine, layer_name)
                if hasattr(layer, "__dict__"):
                    layer.state = self.engine.state

        # Wire nervous -> muscular pathway
        if hasattr(self.engine.layer_02_muscular, "apply_signals") is False:
            def apply_signals(signals):
                for muscle, activation in signals.items():
                    if muscle in self.engine.layer_02_muscular.muscles:
                        self.engine.layer_02_muscular.muscles[muscle].activate(activation)
            self.engine.layer_02_muscular.apply_signals = apply_signals

        # Wire metabolic constraint
        if hasattr(self.engine.layer_05_metabolic, "consume") is False:
            def consume(state):
                fatigue = state.metabolic.get("fatigue", 0)
                for m in state.muscular:
                    state.muscular[m]["force"] *= max(0.2, 1 - fatigue)
            self.engine.layer_05_metabolic.consume = consume

        return {"status": "layers wired"}
