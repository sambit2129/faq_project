from django.urls import path
from .views import some_view  # Ensure views exist

urlpatterns = [
    path('', some_view, name='api_home'),
]
