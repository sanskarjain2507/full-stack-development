from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='shophome'),
    path("about/",views.about,name='Aboutus'),
    path("contact/", views.contact, name='Contactusus'),
    path("tracker/", views.tracker, name='Trackingstatus'),
    path("search/", views.search, name='search'),
    path("productview/", views.productView, name='productView'),
    path("checkout/", views.checkout, name='Checkout'),
    path("products/", views.product_details, name='products'),
    path("test123/", views.test123, name='test123')

    ]