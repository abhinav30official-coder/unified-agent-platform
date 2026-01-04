from pydantic import BaseModel
from typing import Literal

class AgentCreateRequest(BaseModel):
    platform: Literal["vapi", "openai"]
    agent_name: str
    model: str
    instructions: str
