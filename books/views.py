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
        pub_dates = set(Book.objects.all().values_list('pub_date', flat=True))
        pub_dates = sorted([i.strftime('%Y-%m-%d') for i in pub_dates])

        paginator = Paginator(pub_dates, 1)
        page = paginator.get_page(pub_dates.index(value) + 1)

        context['books'] = Book.objects.filter(pub_date=value)
        context['page_obj'] = page
    else:
        context['books'] = Book.objects.all()

    return render(request, template, context)
