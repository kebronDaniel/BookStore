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
    image = models.URLField(max_length=255, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Payment(models.Model):
    PAYMENT_CHOICES = [
        ('c', 'credit card'),
        ('d', 'debit card'),
        ('p', 'paypal')
    ]

    payment_options = models.CharField(max_length=1, null=False, choices=PAYMENT_CHOICES, default='c')
    name_on_the_card = models.CharField(max_length=250, null=False)
    credit_card_number = models.PositiveIntegerField()
    expiration = models.DateTimeField(null=True)
    cvv = models.PositiveSmallIntegerField(null=False)


class ShippingAddress(models.Model):
    address = models.CharField(max_length=255, null=False)
    optionalAddress = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    zip = models.SmallIntegerField(null=False)


class Order(models.Model):
    placed_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, null=False, on_delete=models.PROTECT)
    payment = models.ForeignKey(Payment, null=True, on_delete=models.PROTECT)
    shippingAddress = models.ForeignKey(ShippingAddress, null=True, on_delete=models.PROTECT)
