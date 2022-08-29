from django.contrib import admin
from .models import Book, Genre


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BookAdmin(admin.ModelAdmin):
    # can use exclude
    list_display = ('title', 'author', 'price')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
