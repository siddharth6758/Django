# Generated by Django 4.2.11 on 2024-03-21 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_id', models.CharField(max_length=2)),
                ('seller_id', models.CharField(max_length=2)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=200)),
                ('chat_prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]
