# opti-ml
Research and experimentation with ML, Goal-based AI, and LLMs

## LLM Autonomous Agents

- [Agent Protocol](https://agentprotocol.ai/)

- [AutoGPT Forge: The Blueprint of an AI Agent](https://aiedge.medium.com/autogpt-forge-the-blueprint-of-an-ai-agent-75cd72ffde6)
    - [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432)
    - [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864)

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