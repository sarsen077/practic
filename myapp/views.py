from django.shortcuts import render

# Create your views here.

def uy(request):
    return render(request,template_name='home.html')

def haqqi(request):
    return render(request,template_name='about.html')
