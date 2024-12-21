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
    path('lab9_part1/listbooks/', views.list_books, name='list_books'),
    path('lab9_part1/addbook/', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>/', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>/', views.delete_book, name='delete_book'),
    path('lab9_part2/listbooks/', views.list_books_with_forms, name='list_books_with_forms'),
    path('lab9_part2/addbook/', views.add_book_with_form, name='add_book_with_form'),
    path('lab9_part2/editbook/<int:id>/', views.edit_book_with_form, name='edit_book_with_form'),
    path('lab9_part2/deletebook/<int:id>/', views.delete_book_with_form, name='delete_book_with_form'),
   path('student/', views.list_students, name='list_students'),
    path('add/', views.add_student, name='add_student'),  # Add student
    path('update/<int:pk>/', views.update_student, name='update_student'),  # Update student
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),  # Delete student
   path('students2/', views.list_students2, name='list_students2'),  # List students
    path('students2/add/', views.add_student2, name='add_student2'),  # Add student
    path('students2/update/<int:pk>/', views.update_student2, name='update_student2'),  # Update student
    path('students2/delete/<int:pk>/', views.delete_student2, name='delete_student2'),  # Delete student
   path('', views.list_images, name='list_images'),  # Image list at /images/
    path('upload/', views.upload_image, name='upload_image'),  # Upload image at /images/upload/
]