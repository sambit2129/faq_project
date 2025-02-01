from django.http import JsonResponse


def some_view(request):
    return JsonResponse({"message": "API is working!"})
