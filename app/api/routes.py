from fastapi import APIRouter, HTTPException
from app.schemas.common import AgentCreateRequest
from app.services.agent_service import AgentService

router = APIRouter()
service = AgentService()

@router.post("/agents")
def create_agent(req: AgentCreateRequest):
    try:
        return service.create_agent(req.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=502, detail=str(e))
