from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.FoodInfoViewSet, basename='foodinfo')

urlpatterns = [
    path('', include(router.urls)),  # The FoodInfoViewSet now handles the root endpoint.
    path('health/', views.health_check, name='health_check'),
]
