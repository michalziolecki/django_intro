from django.forms import Form, CharField, ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple

from books.models import BookAuthor, Book


class CategoryForm(Form):
    name = CharField(max_length=256)

    def clean_name(self):
        _name = self.cleaned_data["name"]
        print(f"test={_name}")
        return _name


class AuthorForm(ModelForm):
    class Meta:
        model = BookAuthor
        exclude = []
        # field = "__all__"

    name = CharField(min_length=3, max_length=256, required=True)

    def clean(self):
        result = super().clean()
        print(f"AuthorForm - clean run - result is {result}")
        return result


class BookForm(ModelForm):
    class Meta:
        model = Book
        # exclude = []
        fields = [
            "title",
            "authors",
            "publisher",
            "published_date",
            "categories",
            "average_rating",
        ]

    title = CharField(min_length=3, max_length=256, required=True)

    def clean(self):
        result = super().clean()
        print(f"AuthorForm - clean run - result is {result}")
        return result
