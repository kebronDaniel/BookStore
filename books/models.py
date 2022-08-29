from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    publisher = models.CharField(max_length=255)
    published_year = models.DateTimeField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    placed_at = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, null=False, on_delete=models.PROTECT)


