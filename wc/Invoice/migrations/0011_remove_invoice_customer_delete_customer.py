# Generated by Django 5.0.1 on 2024-03-21 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0010_rename_booked_copulesdetails_is_booked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
