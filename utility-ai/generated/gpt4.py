# Prompt: create a reference implementation of the Utility AI planning technique in python
# Prompt 2: add more logging to the reference implementation
# Prompt 3: give an example of the implementation running 5 times and identifying the best actions
# Prompt 4: update the player health and enemy health within the state
# ChatGPT 4

import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Action:
    def __init__(self, name, utility_function, effect_function):
        self.name = name
        self.utility_function = utility_function
        self.effect_function = effect_function

    def calculate_utility(self, state):
        utility = self.utility_function(state)
        logging.info(f"Calculated utility for action '{self.name}': {utility}")
        return utility

    def execute(self, state):
        self.effect_function(state)
        logging.info(f"Executed action '{self.name}'")

class UtilityAI:
    def __init__(self, actions):
        self.actions = actions

    def decide_and_execute(self, state):
        best_action = None
        highest_utility = float('-inf')

        for action in self.actions:
            utility = action.calculate_utility(state)
            if utility > highest_utility:
                highest_utility = utility
                best_action = action

        logging.info(f"Best action selected: {best_action.name} with utility {highest_utility}")
        best_action.execute(state)

# Example utility functions
def attack_utility(state):
    return state.enemy_health - 10

def defend_utility(state):
    return 100 - state.player_health

# Example effect functions
def attack_effect(state):
    # Assuming each attack reduces enemy health by 20
    state.enemy_health -= 20

def defend_effect(state):
    # Assuming defend action restores 10 player health
    state.player_health += 10
    # Ensure player health does not exceed 100
    state.player_health = min(state.player_health, 100)

# Define actions
actions = [
    Action("Attack", attack_utility, attack_effect),
    Action("Defend", defend_utility, defend_effect)
]

# Create AI
ai = UtilityAI(actions)

# Example state
class State:
    def __init__(self, player_health, enemy_health):
        self.player_health = player_health
        self.enemy_health = enemy_health

    def update(self):
        # Add any additional update logic here
        pass

# Initialize state outside of the simulation loop
current_state = State(player_health=100, enemy_health=100)

# Simulating different states
for i in range(5):
    logging.info(f"Starting Simulation {i+1}: Player Health = {current_state.player_health}, Enemy Health = {current_state.enemy_health}")
    ai.decide_and_execute(current_state)
    current_state.update()
    logging.info(f"End of Simulation {i+1}: Player Health = {current_state.player_health}, Enemy Health = {current_state.enemy_health}\n")
