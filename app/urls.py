from django.urls import path
from . views import *

urlpatterns = [
    path('index', index, name='index'),
    path('shop/<slug:slug>', product_details, name='product_details'),
]