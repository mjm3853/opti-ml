# Prompt: create a reference implementation of the Utility AI planning technique in python
# Prompt 2: add more logging to the reference implementation
# ChatGPT 3.5
# Runs, but not very optimized or understandable

import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UtilityAI:
    def __init__(self):
        self.actions = ["Attack", "Defend"]
        self.utility_values = {
            "Attack": 0,
            "Defend": 0
        }

    def calculate_utility(self, action):
        # Simulate a simple utility function
        if action == "Attack":
            return random.randint(1, 10)
        elif action == "Defend":
            return random.randint(1, 5)

    def select_action(self):
        best_action = None
        best_utility = float("-inf")

        for action in self.actions:
            utility = self.calculate_utility(action)
            if utility > best_utility:
                best_action = action
                best_utility = utility

        logging.info(f"Selected Action: {best_action}, Utility: {best_utility}")
        return best_action

    def update_utilities(self):
        # In a real implementation, you would update utility values based on the game state
        # For simplicity, we'll just randomize them here
        for action in self.actions:
            self.utility_values[action] = random.randint(1, 10)
            logging.info(f"Updated Utility for {action}: {self.utility_values[action]}")

if __name__ == "__main__":
    ai = UtilityAI()

    for _ in range(5):
        ai.update_utilities()
        selected_action = ai.select_action()
        print(f"Selected Action: {selected_action}")
