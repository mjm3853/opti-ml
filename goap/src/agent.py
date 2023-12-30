class Agent:
    def __init__(self, world_state):
        self.world_state = world_state
        self.actions = []
        self.goals = []

    def add_action(self, action):
        self.actions.append(action)

    def add_goal(self, goal):
        self.goals.append(goal)