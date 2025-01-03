# Generated by Django 5.0.1 on 2024-11-13 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryhasproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(related_name='categories', related_query_name='category', through='category.CategoryHasProduct', to='product.product'),
        ),
    ]
