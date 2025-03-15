from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodInfoViewSet

router = DefaultRouter()
router.register(r'', FoodInfoViewSet, basename='foodinfo')

urlpatterns = router.urls

