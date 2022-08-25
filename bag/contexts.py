from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from art.models import Art


def bag_contents(request):
    """ process the contents of the bag"""

    bag_items = []
    art_ids = []
    total = 0
    art_piece_count = 0
    delivery = settings.STANDARD_DELIVERY_FEE
    bag = request.session.get('bag', {})

    for art_id, item_data in bag.items():
        # if isinstance(item_data, int):
        art = get_object_or_404(Art, pk=art_id)
        total += item_data * art.price
        art_piece_count += item_data
        bag_items.append({
            'art_id': art_id,
            'quantity': item_data,
            'art': art
        })
        art_ids.append(art_id)

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'art_piece_count': art_piece_count,
        'grand_total': grand_total,
        'delivery': delivery,
        'art_ids': art_ids
    }

    return context
