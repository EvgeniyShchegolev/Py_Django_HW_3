from django.shortcuts import render, redirect
from .models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    date_to_slug(books)
    context = {'books': books}
    return render(request, template, context)


def show_book(request, slug):
    template = 'books/show_book.html'

    books = Book.objects.all()

    current_book = books.filter(slug=slug)[0]
    try:
        previous_book = books.order_by('-pub_date').filter(pub_date__lt=slug)[0]
    except IndexError:
        previous_book = None
    try:
        next_book = books.order_by('pub_date').filter(pub_date__gt=slug)[0]
    except IndexError:
        next_book = None

    context = {'book': current_book,
               'previous_book': previous_book,
               'next_book': next_book}

    return render(request, template, context)


def date_to_slug(books: Book) -> None:
    for book in books:
        if not book.slug:
            book.slug = str(book.pub_date)
            book.save()
