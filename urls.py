from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet,
    CartViewSet,
    OrderViewSet
)

router = DefaultRouter()

router.register('products', ProductViewSet)
router.register('carts', CartViewSet)
router.register('orders', OrderViewSet)

urlpatterns = router.urls