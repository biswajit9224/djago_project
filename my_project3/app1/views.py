from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def building(request):
    return HttpResponse("building is requeried to create is ciment, iron, chips, water,....")

def temp(request):
    return render(request,'h1.html')