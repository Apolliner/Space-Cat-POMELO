"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

STATIC_URL = '/static/'

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def marketplace(request):
    """Renders the marketplace page."""
    assert isinstance(request, HttpRequest)
    return render(
            request, 
            'app/marketplace.html', 
        {
            'title':'Marketplace',
            'year':datetime.now().year,

        })

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
