from __future__ import absolute_import, unicode_literals
from django.http import JsonResponse
from rest_framework.views import APIView
from tasks.tasks import add

class Add(APIView):
    def get(self, request):
        return JsonResponse({})

    def post(self, request):
        data = request.data
        if "x" in data and "y" in data:
            add.delay(data["x"], data["y"])
            return JsonResponse({ "message": "success"})
        
        return JsonResponse({ "error": "invalid request"})
        