from ninja_extra import status
from ninja_extra.exceptions import APIException


class UniqueException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Объект уже существует"


class PhoneFormatException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Неверный формат номера!"


class InsufficientProductError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Количество превышает текущую доступность товара!"
