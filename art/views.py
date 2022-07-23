from django.shortcuts import render, get_object_or_404
from .models import Art, Category

# Create your views here.


def art_display(request):
    """
    render a display of all the art
    """
    category = request.GET['category']
    art = Art.objects.filter(category=category)

    context = {
        'art': art,
        'category': category,
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
