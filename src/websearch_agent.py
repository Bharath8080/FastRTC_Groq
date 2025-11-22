from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from loguru import logger
import os
from dotenv import load_dotenv
load_dotenv()

# =======================
# 1. LLM MODEL (Groq)
# =======================
model = ChatGroq(
    model="openai/gpt-oss-20b",
    max_tokens=512,
    api_key=os.getenv("GROQ_API_KEY"),
)

# =======================
# 2. TAVILY SEARCH TOOL
# =======================
tavily_tool = TavilySearch(
    max_results=5,
    topic="general",
    api_key=os.getenv("TAVILY_API_KEY")
    # include_answer=True,          # OPTIONAL
    # include_raw_content=False,    # OPTIONAL
    # include_images=False,         # OPTIONAL
)

tools = [tavily_tool]   # 🔥 Replace math tools with Tavily

# =======================
# 3. SYSTEM PROMPT
# =======================
system_prompt = """
You are Samantha, a helpful web-search assistant powered by Tavily.
Always use the Tavily tool when the user asks anything factual, news-related,
current events, or requires real-time information.

Your responses will be converted to audio, so keep them simple, friendly,
and conversational.
"""

# =======================
# 4. MEMORY
# =======================
memory = InMemorySaver()

# =======================
# 5. BUILD THE AGENT
# =======================
agent = create_react_agent(
    model=model,
    tools=tools,
    prompt=system_prompt,
    checkpointer=memory,
)

agent_config = {
    "configurable": {
        "thread_id": "default_user"
    }
}
