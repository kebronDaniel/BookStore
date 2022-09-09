from django.shortcuts import render, redirect
from .models import Book, Genre, ShippingAddress, Payment, Order


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', context={'books': books})


def checkout(request, name, id):

    if request.method == "POST":
        if request.POST['address'] or request.POST['addressTwo'] or request.POST['country'] or request.POST['city'] or request.POST['zip']:
            address = request.POST['address']
            optionalAddress = request.POST['addressTwo']
            country = request.POST['country']
            city = request.POST['city']
            zipcode = request.POST['zip']

            shippingAddress = ShippingAddress(address=address, optionalAddress=optionalAddress, country=country,
                                              city=city, zip=zipcode)
            shippingAddress.save()
        else:
            print("Incomplete form")
        if request.POST['payment_options'] or request.POST['name_on_card'] or request.POST['credit_card_number'] or request.POST['expiration'] or request.POST['cvv']:
            payment_options = request.POST['payment_options']
            name_on_card = request.POST['name_on_card']
            credit_card_number = request.POST['credit_card_number']
            expiration = request.POST['expiration']
            cvv = request.POST['cvv']

            payment = Payment(payment_options=payment_options, name_on_the_card = name_on_card, credit_card_number=credit_card_number,
                              expiration=expiration, cvv=cvv)
            payment.save()
        else:
            print("Incomplete form")

        current_user = request.user
        book = Book.objects.get(pk=id)

        order = Order(user=current_user, book = book, payment=payment, shippingAddress=shippingAddress)
        order.save()

        return redirect('home')

    book = Book.objects.get(pk=id)
    return render(request, 'checkout.html', context={'book':book})


def genres(request):
    all_genres = Genre.objects.all()
    return render(request, 'genres.html', context={'all_genres': all_genres})


def books_list(request, name):
    books_listing = Book.objects.filter(genre__name__contains=name)
    return render(request, 'books.html', context={'books': books_listing})
