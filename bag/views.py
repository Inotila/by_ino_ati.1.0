from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bags contents page """
    return render(request, 'bag/bag.html')


def add_art_to_bag(request, id):
    """ Add art piece to shopping bag"""

    quantity = 1
    redirect_url = request.POST.GET(redirect_url)
    added_to_bag_art = get_object_or_404(Art, pk=id)
    bag = request.session.get('bag', {})

    if id in list(bag.key()):
        bag[id] += quantity
    else:
        bag[id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
