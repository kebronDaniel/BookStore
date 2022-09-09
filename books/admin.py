from django.contrib import admin
from .models import Book, Genre, Order, Payment, ShippingAddress


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BookAdmin(admin.ModelAdmin):
    # can use exclude
    list_display = ('title', 'author', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_options', 'name_on_the_card', 'credit_card_number', 'expiration', 'cvv')


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'optionalAddress', 'country', 'city', 'zip')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)
