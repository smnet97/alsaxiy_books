from django.urls import path

from books.views import BookModelListAPIView, BookDetailAPIView, CategoryBooksAPIView

urlpatterns = [
    path('books/', BookModelListAPIView.as_view(), name='books-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/cat/<int:pk>/', CategoryBooksAPIView.as_view(), name='book-detail-category'),
]