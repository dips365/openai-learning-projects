# Multi-Agent Routing Proof of Concept

This project demonstrates a multi-agent AI assistant that uses the OpenAI SDK (supports both OpenAI API and Azure OpenAI) to classify user queries and route them to specialized agents for relevant responses.

## Features

- **Automatic Agent Selection:**  
  The assistant classifies user queries into one of three categories and routes them to the appropriate agent:
  - 🌍 **PlaceInfoAgent:** Expert in places, travel, countries, and geography.
  - 🎮 **GameInfoAgent:** Expert in video games, board games, and their rules.
  - 💻 **TechInfoAgent:** Expert in technology, programming, and gadgets.

- **Supports Azure OpenAI and OpenAI API**
- **Secure API key management** using `.env` and `python-dotenv`

## Project Structure

multi-agent-routing-poc/ 
├── .env 
├── main.py 
└── README.md


## Setup & Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/dips365/openai-learning-projects.git
    cd openai-learning-projects/multi-agent-routing-poc
    ```

2. **Create a virtual environment (optional but recommended):**
    ```sh
    python -m venv venv
    # On Unix/macOS:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    pip install openai python-dotenv
    ```

4. **Configure your `.env` file:**

    Example for Azure OpenAI:
    ```
    OPENAI_API_TYPE=azure
    ENDPOINT=https://<your-endpoint>.openai.azure.com/
    API_VERSION=2024-12-01-preview
    SUBSCRIPTION_KEY=<your-azure-openai-subscription-key>
    DEPLOYMENT=<your-deployment-name>
    ```

    For OpenAI API, set `OPENAI_API_KEY` instead.

## Usage

Run the main script:

```sh
python main.py
```

Sample output:

```
Agent: game
Answer: Here are three basic rules for cricket: ...

Agent: place
Answer: Japan is known for its beautiful places such as Kyoto, Mount Fuji, and Tokyo...

Agent: tech
Answer: You can create a REST API in Python using frameworks like FastAPI or Flask...
```

How it Works
```
- The script loads environment variables for API credentials.
- It defines three specialized agents with unique system prompts.
- User queries are classified by a routing prompt and sent to the appropriate agent.
- The selected agent generates a response using the OpenAI or Azure OpenAI API.
```

License
This project is licensed under the MIT License.
