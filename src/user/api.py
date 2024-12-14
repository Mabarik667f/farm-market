import logging

from ninja_jwt.authentication import JWTAuth

from user import crud
from user.schemas import (
    AddRole,
    MyTokenRefresh,
    MyTokenVerify,
    Register,
    UserOut,
    UserOutWithEmail,
    MyTokenObtainPairOut,
    MyTokenVerifyOut,
)

from ninja_extra import ControllerBase, api_controller, route
from ninja_jwt.controller import TokenObtainPairController, TokenVerificationController

logger = logging.getLogger("cons")


@api_controller("/users", tags=["users"], permissions=[])
class UserAPI(ControllerBase):
    @route.post("/register", response={201: UserOutWithEmail}, auth=None)
    def register(self, payload: Register):
        return crud.create_user(payload)

    @route.get("/{user_id}", response={200: UserOut}, permissions=[])
    def get_user(self, user_id: int):
        return crud.get_user(user_id)

    @route.delete("/{user_id}", response={204: None})
    def del_user(self, user_id: int):
        crud.get_user(user_id).delete()

    @route.post("/role/{user_id}", response={201: UserOut})
    def add_role(self, user_id: int, role: AddRole):
        crud.add_role(user_id, role)
        return crud.get_user(user_id)

    @route.delete("/role/{user_id}", response={204: UserOut})
    def del_role(self, user_id: int, role: AddRole):
        crud.del_role(user_id, role)
        return crud.get_user(user_id)


@api_controller("/token", tags=["Auth"], auth=None)
class MyTokenObtainPairController(
    TokenObtainPairController, TokenVerificationController
):
    @route.post("/refresh", response=MyTokenObtainPairOut, url_name="token_refresh")
    def refresh_token(self, refresh_token: MyTokenRefresh):
        return refresh_token.output_schema()

    @route.post("/verify", response=MyTokenVerifyOut, url_name="token_verify")
    def verify_token(self, token: MyTokenVerify):
        return token.output_schema()
