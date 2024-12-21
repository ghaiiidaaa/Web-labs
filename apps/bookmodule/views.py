from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from .models import Book
from django.db.models import Q
from .models import Address
from .models import Student
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import BookForm

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
