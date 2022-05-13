from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from users.forms import SignUpForm


class SignUpView(CreateView):
  template_name = 'sign_up.html'
  form_class = SignUpForm
  success_url = reverse_lazy('home')


class UserLoginView(LoginView):
  template_name = 'login.html'
