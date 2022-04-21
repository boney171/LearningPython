from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def helloFunction(request):
    return HttpResponse("Hello Tri, LOL")