from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render

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