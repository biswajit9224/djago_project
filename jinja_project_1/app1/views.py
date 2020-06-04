from django.shortcuts import render

# Create your views here.

def jinja(request):
    d={'who_welcome1':'kanha','who_welcome2':'sonu','who_welcome3':'pinu'}
    d1={'whome':'friends'}
    for data in d:
        return render(request,'jijnja.html',context=d,d1)