# Generated by Django 5.0.1 on 2024-03-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0019_remove_booking_is_booked_event_is_booked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='is_booked',
        ),
        migrations.AddField(
            model_name='booking',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
