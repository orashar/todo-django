from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def todoView(request):
    queryset = TodoItem.objects.all()
    context = {
        "todo_list":queryset
    }
    return render(request, 'todo.html', context)

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, id):
    TodoItem.objects.get(id=id).delete()
    return HttpResponseRedirect('/todo/')