from django.contrib import admin
from .models import Book, Genre, Order


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BookAdmin(admin.ModelAdmin):
    # can use exclude
    list_display = ('title', 'author', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)
