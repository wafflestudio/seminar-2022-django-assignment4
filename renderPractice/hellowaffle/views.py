from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_waffle(*args, **kwargs):
    return HttpResponse(f"hello serverrepairman!")