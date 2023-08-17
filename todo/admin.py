from django.contrib import admin

# Register your models here.
from .models import TodoItem, Category


# Show the TodoItem model fields in the admin page
class TodoItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_completed',
        'category',
        # 'date_started',
        # 'date_completed',
    ]
    # Make the TodoItem model fields clickable
    list_display_links = [
        'id',
        'title',
        'category',
        'is_completed',
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'slug',
    ]
    list_display_links = [
        'title',
        'id',
        'slug'
    ]


admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Category, CategoryAdmin)
