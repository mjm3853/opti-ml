# Prompt: create a reference implementation of the GOAP AI planning technique
# ChatGPT 4
# Works

class Action:
    def __init__(self, cost, preconditions, effects):
        self.cost = cost
        self.preconditions = preconditions
        self.effects = effects

    def check_preconditions(self, world_state):
        return all(world_state.get(k, None) == v for k, v in self.preconditions.items())

    def perform(self, world_state):
        if self.check_preconditions(world_state):
            world_state.update(self.effects)
            return True
        return False

class Goal:
    def __init__(self, priority, conditions):
        self.priority = priority
        self.conditions = conditions

    def is_satisfied(self, world_state):
        return all(world_state.get(k, None) == v for k, v in self.conditions.items())

class Agent:
    def __init__(self, world_state):
        self.world_state = world_state
        self.actions = []
        self.goals = []

    def add_action(self, action):
        self.actions.append(action)

    def add_goal(self, goal):
        self.goals.append(goal)

    def plan(self):
        self.goals.sort(key=lambda g: g.priority, reverse=True)
        for goal in self.goals:
            if goal.is_satisfied(self.world_state):
                continue
            for action in self.actions:
                if action.check_preconditions(self.world_state):
                    return action
        return None

    def execute(self):
        action = self.plan()
        if action:
            return action.perform(self.world_state)
        return False

# Example Usage
world_state = {'hungry': True, 'has_food': True}

agent = Agent(world_state)
agent.add_action(Action(cost=1, preconditions={'hungry': True, 'has_food': True}, effects={'hungry': False}))
agent.add_goal(Goal(priority=1, conditions={'hungry': False}))

success = agent.execute()
print(f"Action executed successfully: {success}")
print(f"World State: {world_state}")
