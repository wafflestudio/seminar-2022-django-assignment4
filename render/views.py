from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main_view(request):
    welcome_string = "Hello, jaeyeong!"
    return HttpResponse(welcome_string)
