# Generated by Django 5.0.1 on 2024-03-05 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0018_booking_is_booked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_booked',
        ),
        migrations.AddField(
            model_name='event',
            name='is_booked',
            field=models.BooleanField(null=True),
        ),
    ]
