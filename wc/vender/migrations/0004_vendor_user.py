# Generated by Django 5.0.1 on 2024-02-06 19:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vender', '0003_alter_vendor_vender_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='vender_profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]