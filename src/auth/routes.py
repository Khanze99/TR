""" Auth routes module """
from fastapi import APIRouter

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@auth_router.get(
    "/me"
)
async def me():
    return {"me": "testuser"}


@auth_router.post(
    "/register"
)
async def register():
    return "OK"
