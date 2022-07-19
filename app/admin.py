from django.contrib import admin
from .models import *


class Product_ImagesInline(admin.TabularInline):
    model = Product_Image
    extra = 1

class Additional_InfoInline(admin.TabularInline):
    model = Additional_Info
    extra = 1

class Product_Admin(admin.ModelAdmin):
    inlines = (Product_ImagesInline, Additional_InfoInline)
    list_display = ('product_name', 'price', 'categories','quantity', 'availability', 'section', 'sku')
    list_editable = ('price', 'categories', 'quantity', 'availability', 'section', 'sku')

# Register your models here.
admin.site.register(Slider)
admin.site.register(Banner)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product,Product_Admin)
admin.site.register(Section)
admin.site.register(Product_Image)
admin.site.register(Additional_Info)




