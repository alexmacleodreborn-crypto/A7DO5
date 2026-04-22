class BehaviourEngine:
    def __init__(self, engine):
        self.engine = engine

    def generate(self, decisions):
        # Convert decisions into coordinated motor commands
        commands = {}

        for decision in decisions:
            if decision == "lift_arm":
                commands.update({
                    "deltoid": 0.6,
                    "biceps_brachii": 0.7
                })

            elif decision == "walk_forward":
                commands.update({
                    "quadriceps": 0.6,
                    "hamstrings": 0.5,
                    "calves": 0.5
                })

        return commands
