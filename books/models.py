from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    publisher = models.CharField(max_length=255)
    published_year = models.DateTimeField()


