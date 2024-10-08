from rest_framework import viewsets
from .models import Author, Category, Book
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer


class AuthorModelView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryModelView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookModelView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer