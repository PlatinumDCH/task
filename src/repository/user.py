from sqlalchemy import select

from src.models import User
from src import sch
async def get_user_by_email():
    pass

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

async def autenticate_user():
    """
    Login user
    - get user by email
    - verify password
    Returned False/User
    """
    pass

async def get_user_by_username():
    pass
