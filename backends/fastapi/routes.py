from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, Depends, status, Body
from fastapi import APIRouter
from datetime import timedelta

from helper import authenticate_user, get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES, users_collection, create_access_token, get_current_user
from models import User, UserCreate, UserInDB, Token

router = APIRouter()

# Routes
@router.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate):
    # Check if user already exists
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    user_data = UserInDB(
        email=user.email,
        hashed_password=get_password_hash(user.password)
    )
    
    result = users_collection.insert_one(user_data.__dict__)
    
    return {
        "id": str(result.inserted_id),
        "email": user.email,
    }

@router.post("/signin", response_model=Token)
async def signin(form_data: UserCreate):
    print(form_data)
    user = authenticate_user(form_data.email, form_data.password)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "username": current_user.username
    }
