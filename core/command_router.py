class CommandRouter:
    def __init__(self, engine):
        self.engine = engine

    def execute(self, command):
        if command == "lift_arm":
            return self._lift_arm()
        elif command == "walk_forward":
            return self._walk_forward()
        else:
            return {"status": "unknown command"}

    def _lift_arm(self):
        return {
            "muscle_groups": ["biceps_brachii", "deltoid"],
            "activation": 0.7
        }

    def _walk_forward(self):
        return {
            "pattern": "gait_cycle",
            "intensity": 0.6
        }
