import random

from django.shortcuts import render


# Create your views here.
def test(request):
    num = random.randint(0, 1000000)
    list = [num, random.randint(0, 100000), random.randint(0, 10000)]
    return render(request, 'restaurant/test.html', {
        'obj': "python variable",
        'bool': True,
        'num': num,
        'list': list,
        'rowcolors': 'blue',
        'url': "i18n/setlang/li/mail-list/list-mail",
    })


def home(request):
    return render(request, 'restaurant/base.html', {})


def about(request):
    return render(request, 'restaurant/about.html', {})


def contact(request):
    return render(request, 'restaurant/about.html', {})
