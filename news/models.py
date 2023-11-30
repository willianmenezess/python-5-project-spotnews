from django.db import models
from news.validators import (
    validate_name, validate_empty, validate_title)


class Category(models.Model):
    name = models.CharField(max_length=200, validators=[validate_name])

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, validators=[validate_name])
    email = models.EmailField(
        max_length=200, unique=True, validators=[validate_name])
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200, validators=[validate_name])

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200, validators=[validate_empty, validate_title])
    content = models.TextField(validators=[validate_empty])
    categories = models.ManyToManyField(Category, related_name="news")  # N:N
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 1:1
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    created_at = models.DateField()

    def __str__(self):
        return self.title
