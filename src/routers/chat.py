from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..api.config import ApiConfig
from ..api.client import ApiClient
from ..decision.decision_maker import DecisionMaker

router = APIRouter()
config = ApiConfig()
api_client = ApiClient(config)
decision_maker = DecisionMaker(api_client)

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = decision_maker.query(request.query)
        decision_maker.parse_response(response)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))