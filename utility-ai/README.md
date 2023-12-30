# Utility AI

## References

- Blog by Tom Looman
    - [Utility AI Part 1](https://www.tomlooman.com/unreal-engine-utility-ai-part1/)
    - [Utility AI Part 2](https://www.tomlooman.com/unreal-engine-utility-ai-part2/)

- Reference Implementation
    - [Easy AI in Unreal Engine](https://medium.com/@morganwalkupdev/easy-ai-in-unreal-engine-c0f4ba1998cc)

- Talks by Dave Marks
    - [Improvign AI Decision Modeling through Utility Theory](https://www.gdcvault.com/play/1012410/Improving-AI-Decision-Modeling-Through)
    - [Building a Better Centaur: AI at Massive Scale](https://www.gdcvault.com/play/1021848/Building-a-Better-Centaur-AI)

- From GPT4:

> Creating a reference implementation of the Utility AI planning technique in Python involves several steps. Utility AI, in the context of game development or decision-making systems, uses a utility function to evaluate and select the best action from a set of possibilities based on certain criteria or states.
> 
> Here's a basic outline of how you can implement this in Python:
> 
> Define Actions: Create a set of actions that the AI can choose from. Each action will have a utility score based on the current state.
> 
> Define State: Define the state of the system. This could be the state of the game world, the state of the AI agent, or any other relevant data that impacts decision-making.
>
> Utility Function: Implement a utility function that calculates a score for each action based on the current state. This function should return higher scores for more desirable actions.
>
> Decision Making: The AI evaluates the utility of each action in the current state and selects the action with the highest utility score.
>
> Execution: The selected action is then executed.
