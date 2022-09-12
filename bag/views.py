from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from art.models import Art


def view_bag(request):
    """ A view that renders the bags contents page """
    return render(request, 'bag/bag.html')


@login_required
def add_to_bag(request, art_id):
    """ Add art piece to shopping bag"""

    art = get_object_or_404(Art, pk=art_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    bag[art_id] = quantity
    messages.success(request, f'Added {art.title} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


@login_required
def remove_from_bag(request, art_id):
    """Remove the item from the shopping bag"""

    try:
        art = get_object_or_404(Art, pk=art_id)
        id = None
        bag = request.session.get('bag', {})
        bag.pop(art_id)
        messages.info(request, f'Removed {art.title} from your bag')
        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item:{e}')
        return HttpResponse(status=500)
