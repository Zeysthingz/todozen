from django.shortcuts import render
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
    try:
        queryset = TodoItem.objects.get(pk=id)
        print(queryset)
        context = {
            'queryset': queryset,
        }
        return render(request, 'todo/todo_detail.html', context)
    except TodoItem.DoesNotExist:
        raise Http404("This task does not exist")
