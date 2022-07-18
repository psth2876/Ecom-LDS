from django.shortcuts import render
from django.db.models import Q
from .models import *

# Create your views here.
def index(request):
    slider_data = Slider.objects.all().order_by('-id')[0:3]
    banner_data = Banner.objects.all().order_by('-id')[0:3]
    main_categories = Main_Category.objects.all()

    product = Product.objects.filter(section__name = "Top Deal Of the Day").filter(availability__gt=0)
    context = {
        'sliders':slider_data,
        'banners':banner_data,
        'main_categories':main_categories,
        'products':product

    }
    return render(request, 'index.html',context)
