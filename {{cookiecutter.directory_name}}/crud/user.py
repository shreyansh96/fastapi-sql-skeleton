from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.user import User
from schemas.user import UserCreate, UserBase


class CRUDUser(CRUDBase[User, UserCreate, UserBase]):
    pass


user = CRUDUser(User)
