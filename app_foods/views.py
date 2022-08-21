import imp
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def food(request):
    return HttpResponse("Hello Food")