from django.shortcuts import render

#4
from django.http import HttpResponse
# Create your views here.

#Just to run the app
def index(request):
    return HttpResponse('My TODO App')
