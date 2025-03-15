from rest_framework import viewsets
from .models import FoodInfo
from .serializers import FoodInfoSerializer

class FoodInfoViewSet(viewsets.ModelViewSet):
    queryset = FoodInfo.objects.all()
    serializer_class = FoodInfoSerializer
