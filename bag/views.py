from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def view_bag(request):
    """ A view that renders the bags contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, art_id):
    """ Add art piece to shopping bag"""

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    bag[art_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, art_id):
    """Remove the item from the shopping bag"""
   
    try:
        id = None
        bag = request.session.get('bag', {})
        bag.pop(art_id)

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
