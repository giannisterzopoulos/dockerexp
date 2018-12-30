from django.shortcuts import render
# from django.http import HttpResponse


def root(request):
    data = {
        'text': 'Hello, templated world!'
    }
    return render(request, 'front/root.html', data)
