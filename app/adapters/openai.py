import openai
from app.adapters.base import AgentAdapter
from app.config import settings
import time
from datetime import datetime


class OpenAIAdapter(AgentAdapter):

    def __init__(self):
        if not settings.OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY is missing")

        openai.api_key = settings.OPENAI_API_KEY

    def create_agent(self, data: dict) -> dict:
        try:
            assistant = openai.beta.assistants.create(
                name=data["agent_name"],
                model=data["model"],
                instructions=data["instructions"]
            )

            return {
                "platform": "openai",
                "agent_id": assistant.id,
                "name": assistant.name,
                "type": "llm",
                "model": assistant.model,
                "created_at": datetime.utcfromtimestamp(
                    assistant.created_at
                ).isoformat() + "Z"
            }
        except Exception as e:
            # VERY IMPORTANT: surface real error
            raise RuntimeError(f"OpenAI API error: {str(e)}")
