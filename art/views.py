from django.shortcuts import render, get_object_or_404
from .models import Art

# Create your views here.


def art_display(request):
    """
    render a display of all the art
    """

    art = Art.objects.all()
    
    context = {
        'art': art,
    }

    return render(request, 'art/art.html', context)


def art_detail(request):
    """
    renders a detailed display of a single art image
    """

    details = Art.get_object_or_404(title)

    context = {
        'details': details,
    }

    return render(request, 'details.html', context)
