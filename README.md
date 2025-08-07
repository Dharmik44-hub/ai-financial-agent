AI Financial Assistant 🤖📈
An interactive financial analysis agent that combines real-time web news with structured stock data to provide comprehensive investment insights. This project uses a multi-agent architecture powered by the phidata framework and Groq's Llama 3 for high-speed inference.

✨ Features
Multi-Agent System: An orchestrator agent intelligently delegates tasks to a specialized Web Search Agent and a Finance Agent.

Real-time Data: Integrates the latest financial news from the web (DuckDuckGo) and market data from Yahoo Finance (yfinance).

Fundamental & Technical Analysis: Provid    es stock fundamentals, analyst recommendations, and technical indicators.

High-Speed LLM: Leverages the Groq API for extremely fast language model responses.

Interactive UI: Built with phidata Playground, providing a clean web interface for interacting with the agent.

🛠️ Tech Stack
Framework: phidata

LLM Provider: Groq (using llama3-70b-8192)

Data Sources: yfinance, duckduckgo-search

Web Server & ASGI: FastAPI, uvicorn

Dependencies: python-dotenv, python-multipart

🚀 Getting Started
Follow these steps to set up and run the project on your local machine.

Prerequisites
Python 3.10+

A Git client

1. Clone the Repository
First, clone the repository to your local machine.

git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME

2. Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

On Windows:

python -m venv myenv
myenv\Scripts\activate

On macOS/Linux:

python3 -m venv myenv
source myenv/bin/activate

3. Install Dependencies
Install all the required Python packages from the requirements.txt file.

pip install -r requirements.txt

4. Set Up Environment Variables
You'll need a Groq API key to run the agent.

Create a file named .env in the root of the project folder.

Add your Groq API key to this file:

# Groq API Key
GROQ_API_KEY="gsk_YourActualGroqApiKeyGoesHere"

▶️ How to Run the Application
Once the setup is complete, run the application using uvicorn. This will start the web server and make the Playground UI available.

uvicorn finance_ai_agent:app --reload --port 7777

finance_ai_agent:app: Tells uvicorn to find the app object inside the finance_ai_agent.py file.

--reload: Enables hot-reloading, so the server restarts automatically when you save code changes.

--port 7777: Runs the server on port 7777.

You can then access the Playground in your browser. The application will print the exact URL in the terminal, which is usually hosted at https://phidata.app/playground. You will need to manually enter your local endpoint (http://localhost:7777) into the UI to connect.

📁 Project Structure
Here is an overview of the project's file structure:

.
├── .env                # Stores secret keys (DO NOT COMMIT TO GIT)
├── .gitignore          # Specifies files and folders for Git to ignore
├── finance_ai_agent.py # Main application logic and agent definitions
├── README.md           # This documentation file
└── requirements.txt    # List of Python dependencies for pip
