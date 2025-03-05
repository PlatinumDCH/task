from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession


from src.database import get_conn_db
import src.repository.user as repo_user
from src.services.token_handler.manager import token_manager, TokenType


class AuthService:

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

    async def get_current_user(
        self,
        token: str = Depends(oauth2_scheme),
        session: AsyncSession = Depends(get_conn_db),
    ):

        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            pyload = await token_manager.decode_token(
                token_type=TokenType.ACCESS, token=token
            )
            email = pyload.get("sub")

            if email is None:
                raise credentials_exception
            
            user = await repo_user.get_user_by_email(email, session)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
            
            return user

        except JWTError:
            raise credentials_exception


auth_service = AuthService()