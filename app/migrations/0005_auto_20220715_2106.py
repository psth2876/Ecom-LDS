# Generated by Django 3.2 on 2022-07-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220715_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product_image',
            name='image_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]