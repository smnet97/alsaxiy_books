from rest_framework.pagination import PageNumberPagination


class BooksPagination(PageNumberPagination):
    page_size = 1
