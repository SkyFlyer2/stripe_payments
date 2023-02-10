from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse

import stripe

from django.conf import settings
from .models import Item


class main_page(TemplateView):
    template_name = 'index.html'


class order_success(TemplateView):
    template_name = 'success.html'


class order_cancelled(TemplateView):
    template_name = 'cancelled.html'


def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(
        request,
        'item_detail.html',
        {'buy_item': item,
         'item_id': id,
         'stripe_key': settings.STRIPE_PUBLISHABLE_KEY,
         }
    )


def item_purchase(request, id):
    item = get_object_or_404(Item, pk=id)
    print('item_purchase', item.price)
#    stripe_amount = item.price.amount * 100    # перевод в центы/копейки
    stripe_amount = str(int(round(item.price.amount, 2) * 100)) # перевод в центы/копейки
    if request.method == 'GET':
        domain_url = settings.DOMAIN_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + (
                    'success?session_id={CHECKOUT_SESSION_ID}'
                    ),
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': item.price.currency,
                        'product_data': {'name': item.name},
                        'unit_amount': stripe_amount,
                        },
                    'quantity': 1,
                    },
                    ],
                mode="payment",
                )
            return JsonResponse({'id': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
