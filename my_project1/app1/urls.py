from django.urls import path

from app1 import views

app_name = 'app1'

urlpatterns = [
    path('My_web/',views.My_web,name ='My_web'),
    path('My_details/',views.My_details,name ='My_details'),
]