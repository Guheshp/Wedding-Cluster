# Generated by Django 5.0.1 on 2024-03-05 14:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0023_delete_cancelvenue'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelVenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=250)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venue.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venue.venue')),
            ],
        ),
    ]
