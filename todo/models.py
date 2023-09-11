from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'category',
            kwargs={
                'slug': self.slug
            }
        )


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date_started = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# TODO:
# 1. Every task needs to have category (work, home, sport, etc.)(FOREIGN KEY)
# 2 Every task needs to have creater (USER)(FOREIGN KEY)
# 3. Every task can have  multiplr tags(MANY TO MANY)
# 4. What is a tag's tasks(ONE TO MANY)
