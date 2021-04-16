from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseServerError, JsonResponse
# Create your views here.


def test(request):
    return HttpResponse("ok")