> [!quote] Harrison Chase, LangChain Creator
> A system is more "agentic" the more an LLM decides how the system can behave.

two way AI and API interact:
* Use API to call a LLM
* LLM call an API

* LangChain & LangGraph are open source frameworks for creating agenting applications.

Terms that you will see in this chapter:
* Agent
	* A system that uses a LLM to decide the control flow of an application
	* Agents are not preprogrammed, they use model to reason and decide the flow of a conversation
	* They can execute tool calls that are suggested by function-calling models
* Function-Calling Model
	* Specialized type of model that considers available functions or tools and suggests when they should be used.
	* They don't call the tool directly, they give that suggestion to agent, who do the calling
* Models
	* Means AI models, can be local can be from web API
* Model Families
	* Multiple models that share a name and architecture
* Toolkit
	* Collection of multiple tools that an agent will use to perform tasks
* Tools or Functions
	* Code that provides extra skills to agent

Tools in this chapter:
* LangChain: Python Library used to create tools and toolkits that allow agents to use your API
* LangGraph: Python library used to create an agent
* Sonnet: Model used to provide reasoning to the LangGraph agent
* Pydantic: Python library used to perform validation in your toolkit

# Creating a LangGraph Agent
* Check out System Card or Model Card of a AI model before using it
	* [Anthropic Model Card](https://www-cdn.anthropic.com/f2986af8d052f26236f6251da62d16172cfabd6e/claude-3-model-card.pdf)

> [!quote] [LangChain Post](https://blog.langchain.com/langgraph-cloud/)
>  Letting an LLM decide the control flow of an application is attractive, as they can unlock a variety of tasks that couldn't previously be automated. In practice, however, it is incredibly difficult to build systems that reliably execute on these tasks.

* LangGraph is a project focused on creating applications that have one or more agents working together.
	* The method LangChain is using is "Legacy Method": allowing more developer control and supporting multi-agent application.
	* It uses terminology from Mathematical Graph Theory like Airflow
		* LangGraph agents = Nodes = Processes that update the state of the application
		* Edges = Flow between one node and another:
			*  LangGraph allow Cyclical Graph: nodes and edges can loop multiple times

> [!tip] Rotating a Credential
> Delete the keys and create new ones when your API got expose or things like that.

> [!danger] `NameError: name '__file__' is not defined`
> Because you append it in interactive shell, you need to create`file.py` and then run it, now it works

# Additional Resources
* [Building Effective AI Agents \\ Anthropic](https://www.anthropic.com/engineering/building-effective-agents)
* [Agents - Google](https://drive.google.com/file/d/1oEjiRCTbd54aSdB_eEe3UShxLBWK9xkt/view)
* [LangGraph](https://langchain-ai.github.io/langgraph/)
* [Introduction | 🦜️🔗 LangChain](https://python.langchain.com/docs/introduction/)
* [Chat models | 🦜️🔗 LangChain](https://python.langchain.com/docs/integrations/chat/)
* [Custom Tools | 🦜️🔗 LangChain](https://python.langchain.com/docs/how_to/custom_tools/)
* [LangChain Overview - Docs by LangChain](https://docs.langchain.com/oss/python/langchain/overview?_gl=1*1xx7lni*_gcl_au*MTQwODEyNDIyMy4xNzYwNTk2NzQ2*_ga*OTU0NjAyMTYyLjE3NjA1ODc4NDU.*_ga_47WX3HKKY2*czE3NjA2ODQwMDAkbzgkZzEkdDE3NjA2ODUwNDMkajYwJGwwJGgw)
* [Messages \| 🦜️🔗 LangChain](https://python.langchain.com/docs/concepts/messages/#aimessage)
* [Converting HumanMessage and AIMessage to Strings in LangChain](https://aiengineerguide.com/blog/convert-humanmessage-aimessage-string-langchain/)
* [Anthropic Model - AvalAI document](https://docs.avalai.ir/fa/models/anthropic)
* [LangChain Overview - Docs by LangChain](https://python.langchain.com/v0.2/docs/concepts/#runnable-interface)
* [OpenAI Platform](https://platform.openai.com/docs/guides/rate-limits/usage-tiers)
* [environment variables - What is the use of python-dotenv? - Stack Overflow](https://stackoverflow.com/questions/41546883/what-is-the-use-of-python-dotenv)