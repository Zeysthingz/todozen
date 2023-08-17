from django.shortcuts import render, get_object_or_404
from .models import TodoItem, Category

from django.http import Http404


# Create your views here.

# Create home page view
def index(request):
    queryset = TodoItem.objects.filter(is_completed=False, user=request.user)
    context = {
        'queryset': queryset,
    }
    return render(request, 'todo/todo_list.html', context)


# Get items by id from database
def todo_detail(request, id):
    query = get_object_or_404(TodoItem, pk=id,user=request.user)
    context = {
        'query': query,
    }
    return render(request, 'todo/todo_detail.html', context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    queryset = TodoItem.objects.filter(is_completed=False, category=category, user=request.user)
    context = {
        'queryset': queryset,
        'category': category,
    }
    return render(request, 'todo/todo_list.html', context)
