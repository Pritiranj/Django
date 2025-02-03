from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def banty(request):
    return HttpResponse('hello')

def sanu(request):
    return HttpResponse('hi i am good')

def india (request):
    return HttpResponse('it is best county ')
