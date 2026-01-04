from abc import ABC, abstractmethod

class AgentAdapter(ABC):

    @abstractmethod
    def create_agent(self, data: dict) -> dict:
        pass
