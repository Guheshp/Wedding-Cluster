# Generated by Django 5.0.1 on 2024-03-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0040_venue_gst_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
