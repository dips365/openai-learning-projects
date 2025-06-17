# Multi-Agent AI Assistant using OpenAI SDK

This project demonstrates a **multi-agent architecture** using the OpenAI SDK (supports both **OpenAI API** and **Azure OpenAI**). It classifies user queries and routes them to specialized agents that provide relevant responses.

## 📌 Features

- 🔄 **Automatic Agent Selection**: Based on user input, the assistant selects one of the following specialized agents:
  - 🌍 **PlaceInfoAgent**: Travel, countries, geography
  - 🎮 **GameInfoAgent**: Games, video games, rules
  - 💻 **TechInfoAgent**: Technology, programming, gadgets

- ✅ **Supports Azure OpenAI or OpenAI API**
- 🛡️ Secure API key management with `.env` and `python-dotenv`

---

## 📂 Project Structure

multi-agent-ai-assistant/
├── agents.py # Main code with agents and routing
├── .env # Environment variables (not tracked in git)
└── README.md

---

## ⚙️ Installation & Setup

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

2️⃣ Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install dependencies:
pip install openai python-dotenv

4️⃣ Setup your .env file:
OPENAI_API_TYPE=azure
ENDPOINT=https://<your-endpoint>.openai.azure.com/
API_VERSION=2024-02-15-preview
SUBSCRIPTION_KEY=<your-azure-openai-subscription-key>
DEPLOYMENT=<your-deployment-name>

🚀 Running the Project
python main.py

Sample Output:
Agent: game
Answer: Here are three basic rules for cricket: ...

Agent: place
Answer: Japan is known for its beautiful places such as Kyoto, Mount Fuji, and Tokyo...

Agent: tech
Answer: You can create a REST API in Python using frameworks like FastAPI or Flask...

📖 Learning Goals
Build multi-agent LLM applications
Use LLMs for classification and task routing
Learn how to securely handle API keys and environment configuration
Integrate OpenAI and Azure OpenAI

📜 License
This project is licensed under the MIT License.