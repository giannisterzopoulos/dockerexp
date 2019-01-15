from django.shortcuts import render
# from django.http import HttpResponse


def root(request):
    data = {
        'text': 'Hello, templated world!',
        'bla': 'bloo',
        'bla2': 'bloo2',

    }
    return render(request, 'frontend/root.html', data)
