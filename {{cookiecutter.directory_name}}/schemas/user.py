from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email_id: Optional[str] = None
    address: Optional[str] = None
    mobile_no: Optional[int] = None
    country_code: Optional[int] = None
    pass


# Properties to receive on item creation
class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


# Properties to return to client
class User(UserBase):
    id: int

    class Config:
        orm_mode = True
