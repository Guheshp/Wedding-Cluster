# Generated by Django 5.0.1 on 2024-02-18 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_customuser_is_vender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_Vender',
            new_name='is_vendor',
        ),
    ]