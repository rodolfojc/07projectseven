from django.shortcuts import render

#4
# Create your views here.

#Just to run the app
def index(request):
    return render(request, 'todo/index.html')
