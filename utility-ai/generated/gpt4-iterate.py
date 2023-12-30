# After many prompts and iterations

import logging
import random

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
    if state.ammo > 0:
        return state.enemy_health - (100 - state.player_health) + 20
    else:
        return -999  # Very low utility if no ammo

def defend_utility(state):
    if state.is_under_attack:
        return (100 - state.player_health) + 15
    else:
        return -10  # Lower utility if not under attack

def find_ammo_utility(state):
    return 100 - state.ammo

# Example effect functions
def attack_effect(state):
    if state.ammo > 0:
        state.enemy_health -= 20  # Damage to the enemy
        state.ammo -= 1  # Use one ammo

def defend_effect(state):
    state.player_health += 10  # Regain some health
    state.player_health = min(state.player_health, 100)

def find_ammo_effect(state):
    state.ammo += 5  # Find some ammo

# Define actions
actions = [
    Action("Attack", attack_utility, attack_effect),
    Action("Defend", defend_utility, defend_effect),
    Action("Find Ammo", find_ammo_utility, find_ammo_effect)
]

# Create AI
ai = UtilityAI(actions)

# Example state
class State:
    def __init__(self, player_health, enemy_health, ammo, is_under_attack):
        self.player_health = player_health
        self.enemy_health = enemy_health
        self.ammo = ammo
        self.is_under_attack = is_under_attack

    def update(self):
        # Randomly determine if the player is under attack
        self.is_under_attack = random.choice([True, False])

# Initialize state
current_state = State(player_health=100, enemy_health=100, ammo=5, is_under_attack=False)

# Simulating different states
for i in range(5):
    logging.info(f"Simulation {i+1} - Player Health: {current_state.player_health}, Enemy Health: {current_state.enemy_health}, Ammo: {current_state.ammo}, Under Attack: {current_state.is_under_attack}")
    ai.decide_and_execute(current_state)
    current_state.update()
    logging.info(f"End of Simulation {i+1} - Player Health: {current_state.player_health}, Enemy Health: {current_state.enemy_health}, Ammo: {current_state.ammo}, Under Attack: {current_state.is_under_attack}\n")
