from enum import Enum
import re
from django.contrib.auth.password_validation import validate_password

from ninja import Schema
from pydantic import EmailStr, field_validator
from pydantic_core.core_schema import FieldValidationInfo

from config.exceptions import UniqueException, PhoneFormatException
from user.exceptions import (
    EmailUniqueException,
    PasswordsMatchException,
    UsernameUniqueException,
    DefaultRoleException,
)
from user.models import CustomUser


class Register(Schema):
    username: str
    email: EmailStr
    password: str
    password2: str


    @field_validator("username")
    def uniqie_username(cls, v):
        try:
            user = CustomUser.objects.filter(username=v)
            if user.exists():
                raise UniqueException
            return v
        except UniqueException:
            raise UsernameUniqueException("Пользователь уже существует!")

    @field_validator("email")
    def uniqie_email(cls, v):
        try:
            user = CustomUser.objects.filter(email=v)
            if user.exists():
                raise UniqueException
            return v
        except UniqueException:
            raise EmailUniqueException("Пользователь уже существует!")


    @field_validator("password")
    def password_check(cls, v):
        validate_password(v)
        return v

    @field_validator("password2")
    def passwords_match(cls, v, info: FieldValidationInfo):
        if "password" in info.data and v != info.data['password']:
            raise PasswordsMatchException()
        return v


class RoleEnum(str, Enum):
    default = "D"
    admin = "A"
    seller = "S"


class Role(Schema):
    name: RoleEnum


class AddRole(Role):
    @field_validator("name")
    def check_role_name(cls, v):
        if v == "D":
            raise DefaultRoleException()
        return v

class RoleOut(Role):
    id: int


class User(Schema):
    username: str


class UserOut(User):
    id: int
    img: str | None = None
    roles: list[Role]


class UserOutWithEmail(UserOut):
    email: EmailStr


class Profile(Schema):
    address: str | None = None
    phone: str | None = None

    @field_validator("phone")
    def regexp_phone_check(cls, v):
        if not v:
            return v

        pattern = re.compile(r"7(\d{10})")
        if pattern.fullmatch(v):
            raise PhoneFormatException("Неверный формат номера!")
        return v


class ProfileOutWithUserId(Profile):
    user_id: int


class ProfileOutWithUser(Profile):
    user: UserOut
