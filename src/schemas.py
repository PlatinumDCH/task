from pydantic import BaseModel, field_validator
from pydantic import EmailStr
import re

class PasswordModel(BaseModel):
    password: str

    @field_validator('password')
    def password_validator(cls, value):
        if len(value) < 5:
            raise ValueError(
                'Password must be at least 5 characters.'
            )
        if not re.search(r'[A-Z]', value):
            raise ValueError(
                'Password must be contain at least one capital letter.'
                )
        if not re.search(r'\d', value):
            raise ValueError(
                'Password must be contain at least one digit.'
                )
        if not re.search(r'[\W_]', value):
            raise ValueError(
                'Password must be contain at least one special character.'
                )
        return value

class UsernameModel(BaseModel):
    username: str

    @field_validator('username')
    def username_valid(cls, value):
        if len(value) < 3 or len(value) > 30:
            raise ValueError(
                'Name must be at 3 - 30 symvol.'
                )
        if not value.isalnum() and "_" not in value:
            raise ValueError(
                'User name may content only letters, digit and underscores.'
                )
        return value

class RegisterUserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator('username')
    def validate_username(cls, value):
        return UsernameModel(username=value).username

    @field_validator('password')
    def validate_password(cls, value):
        return PasswordModel(password=value).password
