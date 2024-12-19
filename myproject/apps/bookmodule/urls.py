from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_books/', views.list_books, name='books.list_books'),
    path('aboutus/', views.aboutus, name='books.aboutus'),  
    path('books/<int:book_id>/', views.one_book, name='books.one_book'),  # This should match the function name
    path('html5/links/', views.links_page, name='links_page'),
    path('html5/text/formatting/', views.text_formatting_page, name='text_formatting_page'),
    path('html5/listing/', views.listing_view, name='listing'),
    path('html5/tables/', views.tables_page, name='tables_page'),
    path('search', views.search_books, name='search_books'),
]