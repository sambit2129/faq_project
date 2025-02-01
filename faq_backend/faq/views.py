from django.shortcuts import render
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from django.http import JsonResponse
from .serializers import FAQSerializer
from django.urls import path
from . import views  # Import your API views here



def home(request):
    return JsonResponse({"message": "Welcome to the FAQ API. Use /api/ to access FAQs."})


def api_home(request):
    return JsonResponse({"message": "Welcome to the API!"})


class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")
        cache_key = f"faqs_{lang}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()
        data = [faq.get_translation(lang) for faq in faqs]
        cache.set(cache_key, data, timeout=300)  # Cache for 5 minutes

        return Response(data)

# Create your views here.
