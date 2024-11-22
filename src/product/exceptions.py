from ninja_extra.exceptions import APIException
from ninja_extra import status

class OneCategoryRequiredForProductError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "У продукта должна быть хотя бы одна категория!"
