# Generated by Django 4.0.4 on 2022-05-14 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_order_partneroffer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='order',
        ),
        migrations.DeleteModel(
            name='partneroffer',
        ),
    ]
