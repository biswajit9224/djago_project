from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def Mobile(request):
    return HttpResponse("my moile name is redme")

def laptop(request):
    return HttpResponse("my laptop is hp")