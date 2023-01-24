from fastapi import APIRouter
from http import HTTPStatus

router = APIRouter(prefix='/ping')


@router.get("/")
async def ping():
    m = {'status_code': HTTPStatus.OK, "message": "pong"}
    return m
