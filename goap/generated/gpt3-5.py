# Prompt: create a reference implementation of the GOAP AI planning technique
# ChatGPT 3.5
# Doesn't run properly

class Action:
    def __init__(self, preconditions, effects):
        self.preconditions = preconditions  # A dictionary of preconditions
        self.effects = effects  # A dictionary of effects

class Agent:
    def __init__(self):
        self.actions = []  # List of available actions
        self.state = {}  # The current state of the agent

    def get_applicable_actions(self):
        applicable_actions = []
        for action in self.actions:
            if all(self.state[k] >= v for k, v in action.preconditions.items()):
                applicable_actions.append(action)
        return applicable_actions

    def plan(self, goal_state):
        plan = []
        while self.state != goal_state:
            applicable_actions = self.get_applicable_actions()
            if not applicable_actions:
                return None  # No plan found
            chosen_action = self.choose_action(applicable_actions)
            plan.append(chosen_action)
            self.apply_action_effects(chosen_action.effects)
        return plan

    def choose_action(self, applicable_actions):
        # Implement a strategy to choose the best action (e.g., A* search)
        return applicable_actions[0]  # Simple example: choose the first applicable action

    def apply_action_effects(self, effects):
        for key, value in effects.items():
            self.state[key] = value

# Example usage
if __name__ == "__main__":
    # Define actions with preconditions and effects
    action1 = Action({"has_weapon": 0}, {"has_weapon": 1})
    action2 = Action({"has_weapon": 1, "at_enemy": 1}, {"attack_enemy": 1})
    action3 = Action({"at_enemy": 1}, {"has_weapon": 0})

    # Create an agent
    agent = Agent()
    agent.actions = [action1, action2, action3]
    agent.state = {"has_weapon": 0, "at_enemy": 0}

    # Define a goal state
    goal_state = {"has_weapon": 1, "attack_enemy": 1}

    # Plan and execute actions to achieve the goal
    plan = agent.plan(goal_state)
    if plan:
        print("Plan found:")
        for action in plan:
            print(f"Action: {action.__class__.__name__}")
    else:
        print("No plan found.")