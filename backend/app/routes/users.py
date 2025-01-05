from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter()

class RegisterUserRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
async def register_user(user: RegisterUserRequest):
    return {"message": f"User {user.email} registered successfully!"}
