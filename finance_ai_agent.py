from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.playground import Playground 
from phi.playground.serve import serve_playground_app
import os


load_dotenv()

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for latest financial news and information",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[DuckDuckGo()],
    add_chat_history_to_messages=True,
    instructions=[
        "Always include sources in your response",
        "Focus on financial news and market analysis",
        "Provide recent and relevant information"
    ]
)


finance_agent = Agent(
    name="Finance AI Agent",
    role="Analyze stocks and provide financial recommendations",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(
        company_news=True,
        technical_indicators=True,
        stock_fundamentals=True,
        analyst_recommendations=True
    )],
    add_chat_history_to_messages=True,
    instructions=[
        "Present data in organized tables",
        "Provide both technical and fundamental analysis",
        "Include risk factors in recommendations"
    ]
)


multi_agent = Agent(
    name="Financial Assistant",
    team=[web_search_agent, finance_agent],
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    instructions=[
        "Combine web information with financial data",
        "Provide comprehensive analysis",
        "Present information in a clear, structured format",
        "Always include both technical and fundamental factors"
    ],
    add_chat_history_to_messages=True,
    markdown=True,
    show_tool_calls=True
)

app = Playground(
    agents=[multi_agent]
).get_app()

if __name__ == '__main__':
    serve_playground_app(app=app,reload=True)