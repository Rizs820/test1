#from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('<h1>Hello, This is Rizwan from T1 Batch and my PRN is 11111.</h1>')


