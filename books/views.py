import json
from uuid import uuid4

from django.core.exceptions import BadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# CBV below
from django.views.generic import ListView, TemplateView, DetailView, FormView, CreateView, UpdateView, DeleteView

from books.forms import CategoryForm, BookForm, AuthorForm
from books.models import BookAuthor, Category, Book


class AuthorListBaseView(View):
    template_name = "author_list.html"
    queryset = BookAuthor.objects.all()

    def get(self, request, *args, **kwargs) -> HttpResponse:
        context = {"authors": self.queryset}
        return render(request, self.template_name, context)


class CategoryListTemplateView(TemplateView):
    template_name = "category_list.html"
    extra_context = {"categories": Category.objects.all()}


class BookListView(ListView):
    template_name = "book_list.html"
    paginate_by = 10
    # queryset = Book.objects.all()
    model = Book


class BookDetailView(DetailView):
    template_name = "book_detail.html"
    model = Book
    # queryset = Book.objects.all()

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))


class CategoryCreateFormView(FormView):
    template_name = "category_base_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")

    def form_valid(self, form):
        result = super().form_valid(form)
        print(f"form = {form}")
        print(f"form.cleaned_data = {form.cleaned_data}")  # cleaned means with removed html indicators
        check_entity = Category.objects.create(**form.cleaned_data)
        print(f"check_entity-id={check_entity.id}")
        return result

    def form_invalid(self, form):
        print(f"form invalid!!! for: {form}")
        return super().form_invalid(form)


class AuthorCreateView(CreateView):
    template_name = "author_form.html"
    form_class = AuthorForm
    success_url = reverse_lazy("author_list")


class AuthorUpdateView(UpdateView):
    template_name = "author_form.html"
    form_class = AuthorForm
    success_url = reverse_lazy("author_list")

    def get_object(self, **kwargs):
        return get_object_or_404(BookAuthor, id=self.kwargs.get("pk"))


class BookCreateView(CreateView):
    template_name = "book_form.html"
    form_class = BookForm
    # success_url = reverse_lazy("book_list")

    def get_success_url(self):
        return reverse_lazy("book_list")

    # def form_valid(self, form):
    #     # something for example logs..
    #     return super().form_invalid(form)

    # def form_invalid(self, form):
    #     # something for example logs..
    #     return super().form_invalid(form)


class BookUpdateView(UpdateView):
    template_name = "book_form.html"
    form_class = BookForm
    # success_url = reverse_lazy("book_list")

    def get_success_url(self):
        return reverse_lazy("book_list")

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))


class BookDeleteView(DeleteView):
    template_name = "book_delete.html"
    model = Book

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse_lazy("book_list")

# FBV below
def get_hello_world(request: WSGIRequest) -> HttpResponse:
    # return HttpResponse("Hello world")
    hello_str: str = "Hello world"
    return render(request, template_name="hello_world.html", context={"hello_var": hello_str})


def get_uuids_list_a(request: WSGIRequest) -> HttpResponse:
    uuids = [str(uuid4()) for _ in range(10)]
    # uuids_as_json = json.dumps(uuids)
    # return HttpResponse(uuids_as_json)
    return render(request, template_name="uuids_list.html", context={"uuids": uuids})


def get_uuids_list_b(request: WSGIRequest) -> JsonResponse:
    uuids = [str(uuid4()) for _ in range(10)]
    return JsonResponse({"uuids": uuids})


def get_argument_from_path(request: WSGIRequest, first_arg: int, second_arg: str, third_arg: str) -> HttpResponse:
    """
    ex. 13
    """
    return HttpResponse(f"first_arg={first_arg}, second_arg={second_arg}, third_arg={third_arg}")


def get_arguments_from_query(request: WSGIRequest) -> HttpResponse:
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    print(type(a))  # str - type casting needed
    print(type(b))  # str
    print(type(c))  # str
    return HttpResponse(f"a={a}, b={b}, c={c}")


@csrf_exempt  # here with that decorator we turn off CSRF in that function
def check_http_query_type(request: WSGIRequest) -> HttpResponse:
    """
    Remember to turn off CSRF token, ONLY FOR TESTS - for a while
    """
    # query_type = "?"
    # if request.method == "GET":
    #     query_type = "to jest GET - tutaj nie powinnismy dodawac i czytac BODY"
    # elif request.method == "POST":
    #     query_type = "to jest POST - tutaj dane leca w BODY"
    # elif request.method == "PUT":
    #     query_type = "to jest PUT - tutaj dane leca w BODY"
    # elif request.method == "DELETE":
    #     query_type = "to jest DELETE - tutaj nie powinnismy dodawac i czytac BODY"
    # """
    # haslo ciekawostka - model dojrzalosci Richardsona
    # https://devkr.pl/2018/04/10/restful-api-richardson-maturity-model/
    # """
    # return HttpResponse(query_type)
    return render(request, template_name="methods.html", context={})


def get_headers(request: WSGIRequest) -> JsonResponse:
    """
    HTTP - text protocol
            HEADERS - some data as dict
            \n\n
            BODY - some data as dict
    """
    headers = request.headers
    return JsonResponse({"headers": dict(headers)})


def raise_error_for_fun(request: WSGIRequest):
    raise BadRequest("My error")
    # return HttpResponse()
