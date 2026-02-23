import phi
import phi.api
from phi.playground import Playground,serve_playground_app
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

import os
load_dotenv()
phi.api=os.getenv("PHI_API_KEY")


# web search agent
web_search_Agent = Agent(
    name="Web Search Agent",
    role="Search the web",
    model=Groq(id="llama-3.1-8b-instant"),
    # tools=[DuckDuckGo()],
    instructions=["always include the source URL in your response"],
    show_tool_calls=True,
    markdown=True
)

# financial agent
financial_Agent = Agent(
    name="Financial Agent",
    role="Analyze financial data",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[YFinanceTools(company_news=True, stock_price=True, stock_fundamentals=True)],
    instructions=["use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

app=Playground(agents=[web_search_Agent, financial_Agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)