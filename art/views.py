from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Art, Category


def art_display(request):
    """
    render a display of all the art
    """
    art = None
    query = None
    category = None
    is_available = None

    if request.GET:
        if 'is_available' in request.GET:
            is_available = request.GET['is_available']
            art = Art.objects.filter(is_available=is_available)
            if not art:
                messages.error(request, "Sorry,the are no art works for sale right now. Please comeback later!")

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            art = Art.objects.filter(category=category)

    if request.GET:
        if 'art-search' in request.GET:
            query = request.GET['art-search']
            queries = Q(title__icontains=query)
            art = Art.objects.filter(queries)
            if not art:
                messages.error(request, "not found")
                return redirect(reverse('art'))

    context = {
        'art': art,
        'category': category,
        'search_term': query
    }

    return render(request, 'art/art.html', context)


def art_detail(request, id):
    """
    renders a detailed display of a single art image
    """

    details = get_object_or_404(Art, pk=id)
    liked = False
    if details.likes.filter(id=request.user.id).exists():
        liked = True

    context = {
        'details': details,
        "liked": liked,
    }

    return render(request, 'art/details.html', context)


def like_item(request, id):
    """handles post likes"""
    details = get_object_or_404(Art, pk=id)

    if details.likes.filter(id=request.user.id).exists():
        details.likes.remove(request.user)
    else:
        details.likes.add(request.user)

    print('liked it')
    return HttpResponseRedirect(reverse('details', args=[id]))
