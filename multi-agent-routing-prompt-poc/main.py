from dotenv import load_dotenv
import os
from openai import OpenAI, AzureOpenAI

load_dotenv()

# Agent System Prompts
AGENTS = {
    "place": "You are an expert in places, travel, countries, and geography. Help the user with their question.",
    "game": "You are an expert in video games, board games, and their rules. Help the user with their question.",
    "tech": "You are an expert in technology, programming, and gadgets. Help the user with their question."
}

# Load environment variables from a .env file
# This ensures sensitive information like API keys are securely loaded
def get_openai_client():
    """
    Returns an OpenAI client based on the environment variables.
    """
    if os.getenv("OPENAI_API_TYPE") == "azure":
        return AzureOpenAI(
            azure_endpoint=os.getenv("ENDPOINT"),
            api_version=os.getenv("API_VERSION"),
            api_key=os.getenv("SUBSCRIPTION_KEY")
        )
    else:
        return OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

def select_agent(user_query):
    routing_prompt = """
    You are a smart classifier. Based on the input, classify it into one of the following categories:
    [place] - for travel, places, geography
    [game]  - for games, gaming, video games
    [tech]  - for technology, programming, gadgets
    Respond ONLY with one of: [place], [game], or [tech].
    """
    openai_client = get_openai_client()
    if openai_client is None:
        raise ValueError("Failed to create OpenAI client. Check your environment variables.")
    response = openai_client.chat.completions.create(
        model=os.getenv("DEPLOYMENT"),
        messages=[
            {"role": "system", "content": routing_prompt},
            {"role": "user", "content": user_query}
        ]
    )
    return response.choices[0].message.content.strip().replace("[", "").replace("]", "")

def ask_agent(agent, user_query):
    system_prompt = AGENTS.get(agent, "You are a general assistant. Help the user with their question.")
    response = get_openai_client().chat.completions.create(
        model=os.getenv("DEPLOYMENT"),
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def handle_user_query(user_query):
    agent = select_agent(user_query)
    if agent:
        answer =  ask_agent(agent, user_query)
        print(f"Agent: {agent}\nAnswer: {answer}")
    else:
        return "Sorry, I couldn't determine the appropriate agent for your query."

if __name__ == "__main__":
    handle_user_query("I am playing cricket. Give me three rules for this game.")
    handle_user_query("What are the best places to visit in Japan?")
    handle_user_query("How do I create a REST API in Python?")

