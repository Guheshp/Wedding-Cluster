# Generated by Django 5.0.1 on 2024-03-03 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0011_rename_aminities_amenities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]
