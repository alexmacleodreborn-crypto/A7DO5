class A7DOState:
    def __init__(self):
        self.time = 0
        self.skeletal = {}
        self.muscular = {}
        self.kinematics = {}
        self.nervous = {}
        self.metabolic = {}
        self.cardiovascular = {}
        self.sensory = {}
        self.avatar = {}
        self.vocal = {}
        self.cognitive = {}
        self.environment = {}

    def update_time(self, dt):
        self.time += dt
