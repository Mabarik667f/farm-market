from ninja_extra import status
from ninja_extra.exceptions import APIException
from config.exceptions import UniqueException


class UsernameUniqueException(UniqueException):
    default_detail = "Пользователь с таким логином уже существует"


class EmailUniqueException(UniqueException):
    default_detail = "Email занят"


class PasswordValidationException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class PasswordsMatchException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Пароли не совпадают"


class DefaultRoleException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Нельзя добавить или удалить роль по умолчанию!"
