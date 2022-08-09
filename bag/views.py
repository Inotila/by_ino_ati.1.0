from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from art.models import Art

# Create your views here.


def view_bag(request):
    """ A view that renders the bags contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, art_id):
    """ Add art piece to shopping bag"""
    
    art = Art.objects.get(pk=art_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    bag[art_id] = quantity
    messages.success(request, f'Added {art.title} to your bag')
    print(bag)

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, art_id):
    """Remove the item from the shopping bag"""

    try:
        id = None
        bag = request.session.get('bag', {})
        bag.pop(art_id)
        print(bag)
        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
