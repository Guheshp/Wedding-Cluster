# Generated by Django 5.0.1 on 2024-02-17 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_remove_customuser_is_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_Vender',
        ),
    ]
