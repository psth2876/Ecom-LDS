# Generated by Django 3.2 on 2022-07-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_model_name_product_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True, verbose_name='post slug'),
        ),
    ]
