from django.forms import Form, CharField


class CategoryForm(Form):
    name = CharField(max_length=256)

    def clean_name(self):
        _name = self.cleaned_data["name"]
        print(f"test={_name}")
        return _name
