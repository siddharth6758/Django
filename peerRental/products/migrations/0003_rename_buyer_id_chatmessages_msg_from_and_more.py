# Generated by Django 4.2.11 on 2024-03-21 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_chatmessages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessages',
            old_name='buyer_id',
            new_name='msg_from',
        ),
        migrations.RenameField(
            model_name='chatmessages',
            old_name='seller_id',
            new_name='msg_to',
        ),
    ]