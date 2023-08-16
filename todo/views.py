from django.shortcuts import render
from .models import TodoItem


# Create your views here.

# Create home page view
def index(request):
    queryset = TodoItem.objects.filter(is_completed=False)
    context = {
        'queryset': queryset,
    }
    return render(request, 'todo/todo_list.html', context)


def todo_detail(request, id):
    queryset = TodoItem.objects.get(pk=id)
    print(queryset)
    context = {
        'queryset': queryset,
    }
    return render(request, 'todo/todo_detail.html', context)
