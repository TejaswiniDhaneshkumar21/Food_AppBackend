from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirect the root URL to the FoodInfo API endpoint
    path('', RedirectView.as_view(url='/api/foodinfo/', permanent=False)),

    # Actual API routes
    path('api/foodinfo/', include('Foodoholic_app.urls')),
]
