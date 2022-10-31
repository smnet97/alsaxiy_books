from django.urls import path

from books.views import BookModelListAPIView, BookDetailAPIView, CategoryBooksAPIView, CategoryListAPIView

urlpatterns = [
    path('books/', BookModelListAPIView.as_view(), name='books-list'),
    path('categories/', CategoryListAPIView.as_view(), name='categories_list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/cat/<int:pk>/', CategoryBooksAPIView.as_view(), name='book-detail-category'),
]
