# Generated by Django 3.2 on 2022-07-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220715_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/product/'),
        ),
        migrations.AlterField(
            model_name='product_image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/product_image/'),
        ),
    ]