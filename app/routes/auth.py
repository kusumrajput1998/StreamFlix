from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(user: dict):
    if user["username"] == "admin" and user["password"] == "admin":
        return {"message": "Login successful!"}
    return {"message": "Invalid credentials"}
