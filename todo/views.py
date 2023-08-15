from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem


# Create your views here.

# Create home page view
def index(request):
    context = {}
    return render(request, 'todo/todo_list.html', context)
