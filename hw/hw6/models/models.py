import datetime
import bcrypt
from pydantic import BaseModel, Field, EmailStr, validator


class UserCreate(BaseModel):
    username: str = Field(..., max_length=10)
    email: EmailStr = Field(..., max_length=50)
    password: str = Field(max_length=128)

    @validator('password')
    def hash_password(cls, value):
        hashed = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    status: str


class OrderOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    status: str

    class Config:
        from_attributes = True
