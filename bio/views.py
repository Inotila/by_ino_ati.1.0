from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages


def bio(request):
    """
    render bio view
    """
    return render(request, 'bio/bio.html',)
