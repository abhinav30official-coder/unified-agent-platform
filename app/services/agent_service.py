from app.adapters.vapi import VapiAdapter
from app.adapters.openai import OpenAIAdapter


class AgentService:

    def create_agent(self, payload: dict) -> dict:
        platform = payload.get("platform")

        if platform == "vapi":
            adapter = VapiAdapter()
        elif platform == "openai":
            adapter = OpenAIAdapter()
        else:
            raise ValueError(f"Unsupported platform: {platform}")

        return adapter.create_agent(payload)
