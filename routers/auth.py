from fastapi import APIRouter, Depends, HTTPException
from models.schemas import User
from fastapi.security import OAuth2PasswordRequestForm
from utils.auth_utils import authenticate_user, create_access_token, get_password_hash
from routers.helper import read_json, write_json

router = APIRouter()

USERS_FILE = "json_files/users.json"

# Register
@router.post("/auth/register")
def register(user: User):
    all_users = read_json(USERS_FILE)
    if user.username in all_users:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    all_users[user.username] = user.dict()
    all_users[user.username]["hashed_password"] = hashed_password
    write_json(USERS_FILE, all_users)
    return user


# Login
@router.post("/auth/login")
def login(logged: OAuth2PasswordRequestForm = Depends()):
    all_users = read_json(USERS_FILE)
    user = authenticate_user(all_users, logged.username, logged.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}



