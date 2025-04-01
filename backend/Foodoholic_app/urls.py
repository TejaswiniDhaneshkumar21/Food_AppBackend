from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
def new_func(router):
    router.register(r'foodinfo', views.FoodInfoViewSet)

new_func(router)

urlpatterns = [
    path('', include(router.urls)), # type: ignore
    path('health/', views.health_check, name='health_check'),
]