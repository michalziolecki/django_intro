from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from users.forms import SignUpForm
from django.core.exceptions import PermissionDenied


class SignUpView(CreateView):
    template_name = 'sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')


class UserLoginView(LoginView):
    template_name = 'login.html'


@login_required
def confirm_user_auth(request):
    # if not request.user.is_authenticated:
    #     print(f"it is {request.user}")
    #     raise PermissionDenied()
    return render(request, template_name="hello_world.html",
                  context={"hello_var": "confirm_user_auth", "is_auth": True})

