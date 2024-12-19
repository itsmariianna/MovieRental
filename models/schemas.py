from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class User(BaseModel):
    username : str = Field(..., min_length=5, max_length=20)
    password : str = Field(..., min_length=6)
    email : EmailStr

class Movie(BaseModel):
    title : str
    genre : str = Field(default=None)
    rating : float = Field(..., ge=0.0, le=10.0)

class Rental(BaseModel):
    user : User
    movie : Movie
    rental_duration : datetime = Field(default_factory=datetime.utcnow)
