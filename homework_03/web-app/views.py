from fastapi import APIRouter


router = APIRouter(prefix="/ping", tags=["PING"])

@router.get("")
def ping():
    return {"message": "pong"}