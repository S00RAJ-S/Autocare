# Generated by Django 4.0.4 on 2022-05-14 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='pid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookings',
            name='rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookings',
            name='wname',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookings',
            name='wphone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
