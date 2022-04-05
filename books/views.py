from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request) -> HttpResponse:
    return HttpResponse("Hello world")

