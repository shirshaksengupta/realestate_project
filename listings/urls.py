from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'), # Passing listing_id to listing.html
    path('search', views.search, name='search'),
]