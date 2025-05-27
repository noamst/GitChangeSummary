🧠 Git Change Summarizer

This is a microservice that automatically summarizes Git diffs using LLMs via LangChain, stores the results in PostgreSQL, and offers a lightweight UI for browsing summaries. It supports dynamic model selection and is easily integrated into GitHub workflows.

🚀 Features

🔁 Summarize Git diffs using LLMs (Groq, OpenAI, Anthropic, etc.)
🔐 Local version , key are supposed be stored server side in .env
📊 Stores summaries in PostgreSQL with commit metadata
🌐 Simple web UI for browsing summaries (/)
⚙️ GitHub Actions integration for automated summarization on push

📦 Tech Stack

Backend: FastAPI + LangChain
Frontend: Jinja2 + Bootstrap
Database: PostgreSQL
Deployment: Docker , locally
CI/CD: GitHub Actions

# Clone repo and enter directory
git clone https://github.com/yourname/GitChangeSummary.git
cd GitChangeSummary

# Set up environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run local DB (or connect to your own)
docker-compose up 
