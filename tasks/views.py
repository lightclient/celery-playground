from __future__ import absolute_import, unicode_literals
from django.http import JsonResponse
from rest_framework.views import APIView
from tasks.tasks import add, mult

def doCalculation(data, calc):
    if "x" in data and "y" in data:
        calc.delay(data["x"], data["y"])
        return JsonResponse({ "message": "success" })
        
    return JsonResponse({ "error": "invalid request" })


class Add(APIView):
    def post(self, request):
        return doCalculation(request.data, add)
        

class Mult(APIView):
    def post(self, request):
        return doCalculation(request.data, mult)