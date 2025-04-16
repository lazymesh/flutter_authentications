from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import Optional
from datetime import datetime
import json

# Models
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    
    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        # print(value, isinstance(value, bytes))
        if isinstance(value, str) or isinstance(value, bytes):
            return cls(**json.loads(value))
        return value

class UserInDB(UserBase):
    hashed_password: bytes
    created_at: datetime = Field(default_factory=datetime.utcnow)

class User(UserBase):
    id: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None