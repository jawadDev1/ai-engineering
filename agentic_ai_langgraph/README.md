# Agentic AI with LangGraph

| Title                                           | Description                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------- |
| [Simple Workflows](./simple_worflows)           | BMI Calculator, LLM calling and LLM chaining workflows using graph nodes edges. |
| [Parallel Workflows](./parallel_workflow)       | Essay evaluation workflow .                                                     |
| [Conditional Workflows](./conditional_workflow) | Review Diagnosis reply workflow, Quadratic equation workflow .                  |

## Generative AI

Generative AI refers to the class of AI models which can generate content, such as text, images, video etc, that resembles human created content.
We have different types of Generative models:

- Text models - GPT 4o, Claude 3.5 Sonnet
- Code models - DeepSeek Coder, Codex
- Image models - Midjourney v6
- Video model - Sora, Runway Gen 3 Alpha

## Agentic AI

Agentic AI is the type of AI which can take up tasks or goal from an user and then move towards completing it with minimal human guidance. Agentic AI can plan, take action, adapt to changes and seek human guidance only when neccessary.
An Agentic AI has different characteristics:

### Authonomous

Agentic ai has the capability to make decisons and perform actions on it's own with getting step by step instructions from a human. We can have different types of autonoumy: - Decision making - Execution - Tool usage
The autonomy of agentic ai can controlled: - Permission scope - define permission what tool ai can use or what decisions ai can make on it's own. - Human-in-the-Loop - Insert checkpoints where ai needs human approval before performing an action for example rejecting a candidte or paying bills - Control override - Allow the human to pause or terminate an ai workflow - Guradrails/Policies - Define strong policies what ai is allowed to do and what not for example deleting user record, or adding new user.

### Goal Oriented

Goal oriented means agents make desicions and perform actions to achieve that perticular defined goal. the goal is store in agent core memory, so all the actions of agent are goal oriented.

### Planning

Planning is the ability of ai to break down high level goals into small tasks or sub-goal and work on them to achieve the desired outcome. AI plans in the following way:

- Create multiple plans
- Test each plan according to their efficiency, cost risk, alignment etc
- Use Human-in-the-Loop to select a Plan

### Reasoning

Reasoning is the ability of ai to understand the goal or information and make descisions. Reasoning is used through out the agent workflow for example in planning, execution, adaptability etc.

### Adaptability

Agent can adapt to changing requirements or planning. The agentic workflow and iterative planning and execution workflow. so if any change comes or agent faces an error, it has the ability to adapt to that change and respond accordingly.

### Context Aware

Agent are context aware of the goal and tasks they have performed yet and the next task the neeed to perform.

## Components

An Agent has mainly 5 components:

- Brain
- Orchestration
- Tools
- Memory
- Supervisor

## Langgraph

Langgraph is an orchestration framework that enables you to build stateful, multi-step and event driven workflows using LLMs. It's ideal for designing both single agent and multi-agent agentic AI applications.

Workflow is a series of tasks that you execute in order to achieve a goal. Now LLM workflow is a workflow where the series of tasks depends on the LLM.

### Graph, Nodes, Edges

In simple terms Nodes are python functions and edges a link that connect one node to another. An Edge tells the orchestrator to what node to execute after current node.

### State

State handles the main and critical info that llm needs to remember. State is global and it is accessible by all the nodes and it is muteable. State keeps evolving through out the cycle of graph.

### Reducers

Reducers in langgraph define how updates from nodes are applied to the shared state.
Each key in the state can have it's own reducer, which determines weather new data replaces, merges or adds to the existing value.

### Langgraph Execution Model

1. Graph Defination - you define the state schema, node and edges
2. Compilation - This checks the graph structure and prepare it for execution
3. Invocation - run the graph with _.invoke(initial_state)_
4. Super-Steps Begin - Execution proceeds in rounds
5. Message Passing & Node Activation - The message are passed to downstream nodes via edges
6. Halting Condition - Execution stops when no nodes are active and no messages are in transit
