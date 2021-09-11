from django.contrib import admin
from django.urls import path, register_converter

from books.views import books_view, index
from books.converters import PubDateConverter

register_converter(PubDateConverter, 'dt')

urlpatterns = [
    path('', index, name='index'),
    path('books/', books_view, name='books'),
    path('books/<dt:value>', books_view),
    path('admin/', admin.site.urls),
]
