from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    """ process the contents of the bag"""

    bag_items = []
    total = 0
    art_piece_count = 0
    delivery = 1000

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'art_piece_count': art_piece_count,
        'grand_total': grand_total,
    }

    return context
