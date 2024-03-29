"""
Definition of urls for Space_Cat_POMELO.
"""

from datetime import datetime
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('marketplace/<int:pk>/', views.product, name='product'),

    #path('about/', views.about, name='about'),
    #path('login/',
    #     LoginView.as_view
    #     (
    #        template_name='app/login.html',
    #         authentication_form=forms.BootstrapAuthenticationForm,
    #         extra_context=
    #         {
    #             'title': 'Log in',
    #             'year' : datetime.now().year,
    #         }
    #     ),
    #     name='login'),
    #path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #path('admin/', admin.site.urls),
]
