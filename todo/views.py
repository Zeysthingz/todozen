from django.shortcuts import render, get_object_or_404
from .models import TodoItem

from django.http import Http404


# Create your views here.

# Create home page view
def index(request):
    queryset = TodoItem.objects.filter(is_completed=False)
    context = {
        'queryset': queryset,
    }
    return render(request, 'todo/todo_list.html', context)


def todo_detail(request, id):
    query = get_object_or_404(TodoItem, pk=id)
    context = {
        'query': query,
    }
    return render(request, 'todo/todo_detail.html', context)
