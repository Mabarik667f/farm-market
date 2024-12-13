import re
import jwt
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.conf import settings
from ninja import Schema
from ninja_jwt.schema import TokenObtainPairInputSchema, TokenVerifyInputSchema
from enum import Enum
from pydantic import EmailStr, field_validator
from pydantic_core.core_schema import FieldValidationInfo

from config.exceptions import UniqueException, PhoneFormatException
from user.exceptions import (
    EmailUniqueException,
    PasswordsMatchException,
    PasswordValidationException,
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
            raise UsernameUniqueException({"detail": {"username": "Пользователь с таким логином уже существует"}})

    @field_validator("email")
    def uniqie_email(cls, v):
        try:
            user = CustomUser.objects.filter(email=v)
            if user.exists():
                raise UniqueException
            return v
        except UniqueException:
            raise EmailUniqueException({"detail": {"email": "Email занят"}})


    @field_validator("password")
    def password_check(cls, v):
        try:
            validate_password(v)
        except ValidationError as e:
            raise PasswordValidationException({"detail": {"password": e.messages}})
        return v

    @field_validator("password2")
    def passwords_match(cls, v, info: FieldValidationInfo):
        if "password" in info.data and v != info.data['password']:
            raise PasswordsMatchException({"detail": {"password": "Пароли не совпадают"}})
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


class MyTokenObtainPairOut(Schema):
    refresh: str
    access: str
    user: UserOut


class MyTokenObtainPair(TokenObtainPairInputSchema):
    def output_schema(self):
        out_dict = self.get_response_schema_init_kwargs()
        out_dict.update(user=UserOut.from_orm(self._user))
        return MyTokenObtainPairOut(**out_dict)


class MyTokenVerifyOut(Schema):
    access: str
    user: UserOut


class MyTokenVerify(TokenVerifyInputSchema):

    def output_schema(self) -> MyTokenVerifyOut:
        payload = jwt.decode(self.token, key=settings.SECRET_KEY, algorithms="HS256")
        user_obj = CustomUser.objects.get(pk=payload["user_id"])
        user = UserOut.from_orm(user_obj)
        return MyTokenVerifyOut(access=self.token, user=user)
