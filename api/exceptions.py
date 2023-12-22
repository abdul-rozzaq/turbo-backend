from rest_framework.exceptions import (
    APIException,
    NotFound,
    PermissionDenied,
    NotAuthenticated,
)


class TokenExpired(NotAuthenticated):
    status_code = 403
    default_detail = "Access token expired"
    default_code = "forbidden"


class ShopNotFound(NotAuthenticated):
    status_code = 403
    default_detail = "Shop not found"
    default_code = "forbidden"