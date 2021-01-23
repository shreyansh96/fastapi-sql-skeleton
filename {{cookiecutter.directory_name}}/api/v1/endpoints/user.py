from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps

router = APIRouter()


@router.post("/", response_model=schemas.User)
async def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Create new item.
    """
    user = await crud.user.create(db=db, obj_in=user_in)
    return user


@router.put("/{id}", response_model=schemas.User)
async def update_user(
    *, db: Session = Depends(deps.get_db), id: int, user_in: schemas.UserUpdate
) -> Any:
    """
    Update an item.
    """
    user = await crud.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = await crud.user.update(db=db, db_obj=user, obj_in=user_in)
    return user


#
#
@router.get("/{id}", response_model=schemas.User)
async def read_user(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """
    Get item by ID.
    """
    user = await crud.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


@router.delete("/{id}", response_model=schemas.User)
async def delete_user(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an item.
    """
    user = await crud.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    user = await crud.user.remove(db=db, id=id)
    return user
