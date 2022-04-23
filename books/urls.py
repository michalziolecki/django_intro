from django.urls import path

from books.views import get_uuids_list_a, get_uuids_list_b, get_argument_from_path, \
    get_arguments_from_query, check_http_query_type, get_headers, raise_error_for_fun, AuthorListBaseView, \
    BookListView, CategoryListTemplateView, BookDetailView, CategoryCreateFormView, AuthorCreateView, BookCreateView, \
    AuthorUpdateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('author-list-base-view/', AuthorListBaseView.as_view(), name="author_list"),
    path('category-list-template-view/', CategoryListTemplateView.as_view(), name="category_list"),
    path('book-list-view/', BookListView.as_view(), name="book_list"),
    path('book-detail/<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('book-delete/<int:pk>/', BookDeleteView.as_view(), name="book_delete"),
    path('category-create/', CategoryCreateFormView.as_view(), name="category_create"),
    path('book-create/', BookCreateView.as_view(), name="book_create"),
    path('book-update/<int:pk>', BookUpdateView.as_view(), name="book_update"),
    path('author-create/', AuthorCreateView.as_view(), name="author_create"),
    path('author-update/<int:pk>', AuthorUpdateView.as_view(), name="author_update"),
    path('uuids_a/', get_uuids_list_a, name="uuids_a"),
    path('uuids_b/', get_uuids_list_b, name="uuids_b"),
    path('path-args/<int:first_arg>/<str:second_arg>/<slug:third_arg>/', get_argument_from_path, name="path_args"),
    path('query-args/', get_arguments_from_query, name="query_args"),
    path('check-http-type/', check_http_query_type, name="check_http_type"),
    path('get-headers/', get_headers, name="get_headers"),
    path('raise-error/', raise_error_for_fun, name="raise_error"),
]
