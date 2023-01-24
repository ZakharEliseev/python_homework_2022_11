from fastapi import APIRouter


router = APIRouter(prefix='/ping')


@router.get("/")
async def ping():
    return {"message": "pong"}
