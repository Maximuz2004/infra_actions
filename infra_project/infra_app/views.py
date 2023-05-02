from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня это снова получилось!')


def second_page(request):
    return HttpResponse('А это та самая вторая страница!')
