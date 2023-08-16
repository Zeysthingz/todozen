from autoslug import AutoSlugField
from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    date_started = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# TODO:
# 1. Every task needs to have category (work, home, sport, etc.)(FOREIGN KEY)
# 2 Every task needs to have creater (USER)(FOREIGN KEY)
# 3. Every task can have  multiplr tags(MANY TO MANY)
# 4. What is a tag's tasks(ONE TO MANY)
