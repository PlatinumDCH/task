from fastapi import HTTPException
from sqlalchemy import select

from src.models import User
from src import sch
from src.services.password_hasher import Hasher

async def get_user_by_email(email, session):
    query = await session.execute(
        select(User).filter(User.email == email)
    )
    user = query.scalars().first()
    return user

async def exist_user(email, session):
    """
    Check if email exist in TableUser, its UnicValue
    """
    query = select(User).filter(
        User.email == email
    )
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user is not None
    
async def create_new_user(body:sch.RegisterUserSchema, session):
    user_data = body.model_dump(by_alias=True)
    new_user = User(**user_data)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

async def autenticate_user(email, password, session):
    """
    Login user
    - get user by email
    - verify password
    Returned False/User
    """
    user = await get_user_by_email(email, session)
    if not user:
        raise HTTPException(
            status_code=404,
            detail='User not found'
        )
    if not Hasher.verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail='Bad Request'
        )
    return user

async def get_user_by_username():
    pass
