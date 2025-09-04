from django.shortcuts import render,redirect
from django.contrib import messages

from.forms import TodoForm
from .models import todo

def index(request):
    item_list=todo.objects.order_by("-date")
    if request.method =="POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form=TodoForm()
    page={
        "forms":form,
        "list":item_list,
        "title":"TODO LIST",
    }
    return render(request,'todo_list/index.html',page)
def remove(request,item_id):
    item=todo.objects.get(id=item_id)
    item.delete()
    messages.info(request,"item removed")
    return redirect("todo")

# Create your views here.

