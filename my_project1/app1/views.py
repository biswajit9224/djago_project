from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def My_web(request):
    return HttpResponse("<p>It Is My <u><b>1st Web</u></b> Page In django</p>")

def My_details(request):
    return HttpResponse("<h1><b>my details</b></h1><br><p>My name is Biswajit Dash <br> I am from Odisha <br> I have complited my b-tec in Electrical Engennring ")
