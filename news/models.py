from django.db import models
from news.validators import validate_name


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
