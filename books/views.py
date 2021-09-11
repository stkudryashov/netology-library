from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator

from books.models import Book


def index(request):
    return redirect('books/')


def books_view(request, value=None):
    template = 'books/books_list.html'
    context = dict()

    if value:
        books = Book.objects.all()

        paginator = Paginator(books, 1)
        page = paginator.get_page(1)

        context['books'] = books
    else:
        context['books'] = Book.objects.all()

    return render(request, template, context)
