from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src import get_conn_db
from src import sch

from src.services.password_hasher import Hasher
from src.services.token_handler.manager import TokenType, token_manager
from src.services.auth import auth_service
import src.repository.user as repo_user

router = APIRouter(prefix='/auth')

@router.post(
        '/register',
        status_code=200
    )
async def register_user(
    body: sch.RegisterUserSchema,
    session = Depends(get_conn_db)
):
    """
    Register user in database.

    **Body request (RegisterUserSchema):**
    - `name`: str
    - `email`: EmailStr
    - `full_name`: str|None
    - `password`: str

    **Response (RegisterUserResponseSchema):**
    - `name`: str
    - `email`: EmailStr
    - `full_name`: str|None
    """
    if await repo_user.exist_user(
        body.email, session
    ):
        raise HTTPException(
            status_code=409,
            detail='User already exists'
        )
    body.password = Hasher.get_password_hash(body.password)
    new_user = await repo_user.create_new_user(body, session)
    response_user = sch.RegisterUserResponseSchema.model_validate(new_user)
    return response_user.model_dump(exclude={"password"})

@router.post('/login')
async def login_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session = Depends(get_conn_db)
):
    user = await repo_user.autenticate_user(
        form_data.username,
        form_data.password,
        session
    )
    encode_access_token = await token_manager.create_token(
        token_type=TokenType.ACCESS,
        data={"sub": user.email},
    )
    
    return sch.TokenResponseSchema(
        access_token=encode_access_token,
    ).model_dump()

@router.get('/me')
async def get_me(user = Depends(auth_service.get_current_user)):
    return {
        'username': user.name,
        'email': user.email
    }

