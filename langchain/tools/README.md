# Tool

A tool is just a python function (or API) that is packaged in a way the LLM can understand and call when needed.
LLMs can process data, do reasoning , make decisions but they can't perform an action on their own, to perform some action they need a tool.

LLMs can't do things like:

- Access Live Data
- Call API's
- Run code
- Interact with database

## Built-In Tools

Langchain has some built-in tools like DuckDuckGoSearchFun, ShellTool, PythonREPLTool etc.
[View List of Tools](https://reference.langchain.com/python/langchain-community/tools)

```example
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke("Who is monkey D. luffy")

print(results)
```

## Custom Tools

Langchain also allows to built custom tools.

There are 3 ways to create a custom tool

1. @tool decorator
2. Using StructuredTool & Pydantic
3. BaseTool Class

A structured tool in LangChain is a special type of tool where the input to the tool follows a structured schema, typically defined using a pydantic model.

## Toolkit

A toolkit is just a collection of related tools, that serves a common purpose.
You can group related tools into a toolkit.

## Tool Binding

Tool binding is a step where you register tools with a Large Language Model so that:

- LLM knows what tools are available.
- It knows what each tool does.
- It knows what input format to use (via schema).

## Tool Calling

Tool calling is the process where LLM decides, during a conversation or task, that it needs to use a specific tool and generates a structured output with:

- the name of tool
- the arguments to call it with

The LLM does not actually run the tool, it just suggests the tool and the input arguments. The actual execution is handled by the langchain or us.

## Tool Execution

Tool execution is the step where the actual python function (tool) is run using the input arguments that the LLM suggested during tool calling.
