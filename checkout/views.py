from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderFrom


def checkout(request):
    bag = request.session.get('bag')
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('art'))

    order_form = OrderFrom()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)