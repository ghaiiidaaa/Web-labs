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