from pydantic import BaseModel, EmailStr

class User(BaseModel):
  email: EmailStr
  hashed_password: str

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  username: str | None = None


