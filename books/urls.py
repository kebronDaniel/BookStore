from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name="index"),
    path('genres/', views.genres, name="genres"),
    path('genres/<str:name>', views.books_list, name="list"),
    path('genres/<str:name>/<int:id>', views.checkout, name="checkout"),
]