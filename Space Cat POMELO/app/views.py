"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import product_db


STATIC_URL = '/static/'

def home(request):
    name_product = ''
    description_product = ''
    image_product = ''
    price_product = ''
    product_card = ''

    for i in range(len(product_db)):
        product_card += (f'<div class="card-horizontal-scroll">'
                        f'<a href="/marketplace/{i}/"><img src="{product_db[i]["image"]}" class=card-image></a>'
                        f'<h3 class="card-title"><a href="/marketplace/{i}/" class="white">{product_db[i]["name"]}</a></h3></div>')

    context = {
        'title': 'Space Cat homepade!',
        'product_card': product_card,
        }
    return render(request, 'app/index.html', context)
#--------------------------------------------------------------------------------------------------------------------

def marketplace(request):
    """Renders the marketplace page."""
    product_card = ''

    for i in range(len(product_db)):
        product_card += (f'<div class="card">'
                        f'<a href="/marketplace/{i}/"><img src="{product_db[i]["image"]}" class=card-image></a>'
                        f'<h3 class="card-title"><a href="/marketplace/{i}/" class="white">{product_db[i]["name"]}</a></h3></div>')
    context = {
        'title': 'Marketplace',
        'product_card': product_card,
        }

    assert isinstance(request, HttpRequest)
    return render(request, 'app/marketplace.html', context)
def product(request, pk):
    """Renders the product."""
    name_product = product_db[pk]["name"]
    description_product = product_db[pk]["description"]
    image_product = product_db[pk]["image"]
    price_product = product_db[pk]["price"]

    context = {
        'title': name_product,
        'name_product': name_product,
        'description_product': description_product,
        'image_product': image_product,
        'price_product': price_product,
        }

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/product.html',
        context
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
