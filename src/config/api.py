from ninja import NinjaAPI
from user.api import router as user_router
from product.api import router as product_router
from cart.api import router as cart_router
from category.api import router as category_router
from order.api import router as order_router

api = NinjaAPI()

api.add_router("/users/", user_router)
api.add_router("/cart/", cart_router)
api.add_router("/products/", product_router)
api.add_router("/categories/", category_router)
api.add_router("/orders/", order_router)
