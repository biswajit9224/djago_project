from django.urls import path

from app2_1 import views

app_name='app2_1'

urlpartterns = [
    path('Mobile/',views.Mobile,name='Mobile'),
    path('laptop/',views.laptop,name='laptop')
]