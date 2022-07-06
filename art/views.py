from django.shortcuts import render
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
