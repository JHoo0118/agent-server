from pydantic import BaseModel, EmailStr, Field


class SignupRequest(BaseModel):
    email: EmailStr = Field()
    password: str = Field()
    username: str = Field()
