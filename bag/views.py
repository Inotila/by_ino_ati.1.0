from django.shortcuts import render, redirect

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
    print(request.session['bag'])
    return redirect(redirect_url)
