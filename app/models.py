from django.db import models
from ckeditor.fields import RichTextField
from .utils import generate_new_slug 
from django.urls import reverse


# Create your models here.
class Slider(models.Model):

    discount_choices = (
        ('HOT DEALS', 'HOt Deals'),
        ('NEW ARRIVALS', 'New Arrivals'),
        ('SPECIAL OFFERS', 'Special Offers'),
        ('TOP RATED', 'Top Rated'),
        ('BEST SELLER', 'Best Seller'),
    )

    # title = models.CharField(max_length=100)
    # description = models.TextField()
    brand = models.CharField(max_length=100)
    discount_deal = models.CharField(choices=discount_choices,max_length=100)
    sale = models.IntegerField()
    brand = models.CharField(max_length=200)
    discount = models.IntegerField()
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/slider/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

class Banner(models.Model):
    image = models.ImageField(upload_to='media/banner/')
    discount_deal = models.CharField(max_length=100)
    quote = models.CharField(max_length=100)
    discont = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quote

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

class Main_Category(models.Model):
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='media/main_category/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Main Category'
        verbose_name_plural = 'Main Categories'

class Category(models.Model):
    name = models.CharField(max_length=100)
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.main_category.name + " --- " + self.name  

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Sub_Category(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.main_category.name  + " -- "+ self.category.name  + " -- " + self.name 

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

class Section(models.Model):
    name = models.CharField(max_length=100)
    # sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(verbose_name="post slug",unique=True,null=True,blank=True,editable=False)
    price = models.IntegerField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = RichTextField()
    product_information = RichTextField(null=True)
    discount = models.IntegerField()
    quantity = models.IntegerField()
    availability = models.IntegerField()
    image = models.ImageField(upload_to='media/product/',blank=True,null=True)
    image_url = models.CharField(max_length=200,null=True)
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
    tags = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def save(self,*args, **kwargs):
        self.slug = generate_new_slug(self.__class__,self.product_name)
        return super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('product_details',kwargs={'slug':self.slug}) 

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product_image/',blank=True,null=True)
    image_url = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

class Additional_Info(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'Additional Info'
        verbose_name_plural = 'Additional Infos'
