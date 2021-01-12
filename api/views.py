from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def showtext(request):
    return HttpResponse("Hello")
