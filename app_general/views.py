from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello")