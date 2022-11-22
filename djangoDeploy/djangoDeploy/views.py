from django.http import HttpResponse


def index(request):
    return HttpResponse('hello 김유신!')
