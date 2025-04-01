from django.http import HttpResponse
from rest_framework import viewsets
from .models import FoodInfo
from .serializers import FoodInfoSerializer

class FoodInfoViewSet(viewsets.ModelViewSet):
    queryset = FoodInfo.objects.all()
    serializer_class = FoodInfoSerializer

def health_check(request):
    return HttpResponse("OK", status=200)