from django.contrib import admin

# Register your models here.
from .models import TodoItem


# Show the TodoItem model fields in the admin page
class TodoItemAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_completed',
        # 'date_started',
        # 'date_completed',
    ]


admin.site.register(TodoItem, TodoItemAdmin)
