# Generated by Django 3.2 on 2022-07-15 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20220715_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additional_info',
            name='details',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='additional_info',
            name='specification',
            field=models.CharField(max_length=200),
        ),
    ]
