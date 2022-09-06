from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Art, Category


def art_display(request):
    """
    render a display of all the art
    """
    art = None
    query = None
    category = None
    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            art = Art.objects.filter(category=category)

    if request.GET:
        if 'art-search' in request.GET:
            query = request.GET['art-search']
            queries = Q(title__icontains=query)
            art = Art.objects.filter(queries)
            print(f'art is {art}')
            if not art:
                print('no art')
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

    context = {
        'details': details,
    }

    return render(request, 'art/details.html', context)
