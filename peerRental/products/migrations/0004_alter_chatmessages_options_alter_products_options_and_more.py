# Generated by Django 4.2.11 on 2024-03-29 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rentapplication'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessages',
            options={'verbose_name_plural': 'Chats'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='rentapplication',
            options={'verbose_name_plural': 'Rent-Applications'},
        ),
    ]
