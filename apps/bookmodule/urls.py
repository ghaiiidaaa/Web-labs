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
    path('simple/query/', views.simple_query, name='simple_query'),
    path('complex/query/', views.lookup_query, name='lookup_query'),
    path('lab8/task1/', views.lab8_task1, name='lab8_task1'),
    path('lab8/task2/', views.lab8_task2, name='lab8_task2'),
    path('lab8/task3/', views.lab8_task3, name='lab8_task3'),
    path('lab8/task4/', views.lab8_task4, name='lab8_task4'),
    path('lab8/task5/', views.lab8_task5, name='lab8_task5'),
    path('students/city_count/', views.city_count, name='city_count'),
    path('students/list/', views.student_list, name='student_list'),
]