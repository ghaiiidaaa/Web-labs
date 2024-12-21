from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q, Count, Sum, Avg, Max, Min

from .models import Book, Address, Student, Student2, Address2, ImageModel
from .forms import BookForm, StudentForm, AddressForm, Student2Form, Address2Form, ImageForm




def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'books/list_books.html')

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')

def home(request):
    return render(request, "bookmodule/home.html")  # Create a home.html template

def one_book(request, book_id):  # Make sure this function is named exactly as referenced
    # Here, you can fetch book details from the database based on book_id, or render the page with the book_id
    return render(request, 'books/one_book.html', {'book_id': book_id})

def links_page(request):
    return render(request, 'books/links.html')

def text_formatting_page(request):
    return render(request, 'books/formatting.html')

def listing_view(request):
    return render(request, 'books/listing.html')

def tables_page(request):
    return render(request, 'books/tables.html')

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

# Search view
def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        # Filter books based on input
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)
        
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')


BOOKS = [
    {"id": 1, "title": "Continuous Delivery and DevOps", "author": "J. Humble", "price": 150.0, "edition": 3, "description": "Guide to modern software delivery."},
    {"id": 2, "title": "DevOps Principles", "author": "Gene Kim", "price": 120.0, "edition": 1, "description": "Learn about DevOps culture."},
    {"id": 3, "title": "Machine Learning Guide", "author": "Andriy Burkov", "price": 95.0, "edition": 2, "description": "Introduction to ML concepts."},
    {"id": 4, "title": "Reverse Engineering Secrets", "author": "E. Eilam", "price": 100.0, "edition": 3, "description": "In-depth reverse engineering techniques."},
    {"id": 5, "title": "Data Science and Machine Learning", "author": None, "price": 110.0, "edition": 4, "description": "Practical guide to data science."},
    {"id": 6, "title": "The Art of Software Testing", "author": "Glenford Myers", "price": 50.0, "edition": 3, "description": "Classic book on software testing."}
]




def simple_query(request):
    # Filter books where 'and' is in the title
    mybooks = [book for book in BOOKS if 'and' in book['title'].lower()]
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lookup_query(request):
    # Filter books based on multiple conditions
    mybooks = [
        book for book in BOOKS
    if 'and' in book['title'].lower() and
       book['edition'] >= 2 and
       book['price'] > 100 and
       book['author'] is not None
    ]
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})




def lab8_task1(request):
    books = Book.objects.filter(price__lte=50)
    return render(request, 'bookmodule/task1.html', {'books': books})

def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})


from django.db.models import Count, Sum, Avg, Max, Min

def lab8_task5(request):
    aggregations = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'aggregations': aggregations})


def some_view_function(request):
    books = Book.objects.all()
    return render(request, 'template.html', {'books': books})

def city_count(request):
    counts = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/city_count.html', {'counts': counts})


def student_list(request):
    students = Student.objects.select_related('address')  # Use select_related for optimized query
    return render(request, 'bookmodule/student_list.html', {'students': students})


def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return HttpResponseRedirect('/books/lab9_part1/listbooks/')
    return render(request, 'bookmodule/addbook.html')


def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return HttpResponseRedirect('/books/lab9_part1/listbooks/')
    return render(request, 'bookmodule/editbook.html', {'book': book})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return HttpResponseRedirect('/books/lab9_part1/listbooks/')

def list_books_with_forms(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks_with_forms.html', {'books': books})



def add_book_with_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/lab9_part2/listbooks/')
    else:
        form = BookForm()
    return render(request, 'bookmodule/addbook_with_form.html', {'form': form})


def edit_book_with_form(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/lab9_part2/listbooks/')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/editbook_with_form.html', {'form': form})



def delete_book_with_form(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect('/books/lab9_part2/listbooks/')





def list_students(request):
    students = Student.objects.select_related('address').all()  # Fetch all students
    print("DEBUG: Students fetched:", students)  # Debug output
    return render(request, 'students/list.html', {'students': students})  # Ensure this matches your template file




def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': form})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/update.html', {'form': form})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'students/delete.html', {'student': student})

def list_students2(request):
    students = Student2.objects.prefetch_related('addresses').all()
    return render(request, 'students/list2.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form()
    return render(request, 'students/add2.html', {'form': form})

def update_student2(request, pk):
    student = get_object_or_404(Student2, pk=pk)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form(instance=student)
    return render(request, 'students/update2.html', {'form': form})

def delete_student2(request, pk):
    student = get_object_or_404(Student2, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students2')
    return render(request, 'students/delete2.html', {'student': student})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')  # Redirect to the list page after upload
    else:
        form = ImageForm()
    return render(request, 'images/upload.html', {'form': form})


def list_images(request):
    images = ImageModel.objects.all()
    for img in images:
        print(f"DEBUG: Title={img.title}, URL={img.image.url}, Path={img.image.path}")
    return render(request, 'images/list.html', {'images': images})