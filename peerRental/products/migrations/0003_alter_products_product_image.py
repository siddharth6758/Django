# Generated by Django 4.2.11 on 2024-03-19 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_rent_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.FileField(upload_to='products/'),
        ),
    ]
