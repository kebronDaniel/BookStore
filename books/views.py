from django.shortcuts import render
from .models import Book, Genre


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', context={'books': books})


def checkout(request, name, id):
    book = Book.objects.get(pk=id)
    return render(request, 'checkout.html', context={'book':book})


def genres(request):
    all_genres = Genre.objects.all()
    return render(request, 'genres.html', context={'all_genres': all_genres})


def books_list(request, name):
    books_listing = Book.objects.filter(genre__name__contains=name)
    return render(request, 'books.html', context={'books': books_listing})
