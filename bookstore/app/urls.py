from django.urls import path

from .views import *

urlpatterns = [
    path('add_book/', addBook),
    path('get_all_books/', retrieveAllBooks),
    path('get_specific_book/', retrieveSpecificBook),
    path('update_book_details/', updateBookDetails),
    path('delete_book/', deleteBook),

]
