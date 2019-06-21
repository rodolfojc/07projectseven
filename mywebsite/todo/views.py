from django.shortcuts import render, redirect
from django.views.decorators.http import request_POST

#4
# Create your views here.
from .form import TodoForm
from .models import Todo

#Just to run the app
def index(request):
    mytodo = Todo.object.order_by('id')
    form = TodoForm()
    context = { 'mytodo' : mytodo, 'form' : form }
    return render(request, 'todo/index.html', context)

@require_POST
def addNewTodo(request):
    form = TodoForm(request_POST)

    if form.is_valid():
        my_new_todo = Todo(todotext=request.POST['text'])
        my_new_todo.save()

    return redirect('index')
