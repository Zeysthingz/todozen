from django.db import models


# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    date_started = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
