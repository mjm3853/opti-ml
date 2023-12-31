# Utility AI

## Comparing GOAP vs. Utility AI

- Via GPT4


When deciding between Goal-Oriented Action Planning (GOAP) and Utility AI for a conversational AI system, it's important to consider the specific requirements and characteristics of your application. Both systems have their strengths and are suited to different types of tasks.

GOAP (Goal-Oriented Action Planning)
Planning-Based: GOAP is a planning-based system where actions are chosen based on goals. It's effective in situations where actions must be planned and sequenced to achieve specific objectives.

Structured Decision Making: GOAP works well in environments with clear, defined goals and where actions can be planned in advance to achieve these goals.

Predictability: The behavior of a GOAP-based system is often more predictable and structured, which is beneficial for tasks requiring consistency and adherence to a predefined plan.

Complexity in Implementation: Implementing a GOAP system can be more complex due to the need for defining goals, actions, and the planning algorithm.

Utility AI
Contextual Decision Making: Utility AI evaluates actions based on a utility function, which can change dynamically according to the context. This makes it suitable for environments where decisions need to be made based on changing states or inputs.

Flexibility: It’s more flexible than GOAP and can easily adapt to new conditions or criteria by adjusting utility functions.

Simplicity in Implementation: Generally, Utility AI is simpler to implement and understand, as it involves scoring actions based on current context without the need for complex planning algorithms.

Suitability for Conversational Systems: In conversational AI, responses often need to adapt dynamically to the user's input, mood, and the ongoing context. Utility AI’s strength in handling dynamic and contextual information makes it potentially more suitable for this.

Conclusion
For a conversational AI system, Utility AI is generally more appropriate. Conversational AI often requires dynamic response generation based on the current context of the conversation, user mood, and other real-time factors. Utility AI’s ability to evaluate and score potential responses based on the current state makes it better suited for this task. GOAP, while powerful in goal-oriented and planning-heavy contexts, may be too rigid and structured for the fluid nature of human conversation.

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
