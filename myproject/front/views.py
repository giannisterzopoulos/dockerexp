from django.shortcuts import render


def home(request):
    data = {}
    return render(request, 'front/home.html', data)
