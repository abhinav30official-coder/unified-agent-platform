import requests
from app.adapters.base import AgentAdapter
from app.config import settings
from datetime import datetime

class VapiAdapter(AgentAdapter):
    BASE_URL = "https://api.vapi.ai/assistant"

    def create_agent(self, data: dict) -> dict:
        if not settings.VAPI_API_KEY:
            raise RuntimeError("VAPI_API_KEY is missing")

        headers = {
            "Authorization": f"Bearer {settings.VAPI_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "name": data["agent_name"],
            "model": {
                "provider": "openai",
                "model": data["model"]
            },
            "firstMessage": data["instructions"]
        }

        

        response = requests.post(
            self.BASE_URL,
            headers=headers,
            json=payload,
            timeout=10
        )

        if response.status_code >= 400:
            raise RuntimeError(
                f"Vapi API error: {response.status_code} - {response.text}"
            )
        data = response.json()
        return {
            "platform": "vapi",
            "agent_id": data["id"],
            "name": data["name"],
            "type": "voice",
            "model": data["model"]["model"],
            "created_at": data["createdAt"]
        }
