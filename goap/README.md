# GOAP = Goal Oriented Action Planning

## Reference Implementation

### Part 1
[NPC AI with GOAP 1 - Understanding and Approach](https://pankajbasnal17.medium.com/npc-ai-with-goap-1-understanding-and-approach-908312ba7067)

- Agent
    - Planner - i.e. with A* algorithm
        - Generated Graph of actions and impact to state from memory and current state
        - Should lead to Goal State
    - Goals - Desired state
    - State - collection of facts about the environment
    - Sensors - how the agent observes the environment
    - Action - a unit of behavior to modify state
        - Has Preconditions
        - Can be Executed
        - May be Simulated
    - Memory - TBD
- Objects
    - State
    - Actions

### Part 2
[NPC AI with GOAP 2: Implementation Of Framework](https://pankajbasnal17.medium.com/npc-ai-with-goap-2-implementation-of-framework-10c47e624964)