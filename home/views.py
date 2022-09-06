from django.shortcuts import render


def index(request):
    """
    render index view
    """
    return render(request, 'home/index.html')
