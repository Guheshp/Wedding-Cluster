# Generated by Django 5.0.1 on 2024-03-05 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0020_remove_event_is_booked_booking_is_booked'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancleVenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=250)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venue.event')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venue.venue')),
            ],
        ),
    ]
