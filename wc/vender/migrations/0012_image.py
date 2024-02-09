# Generated by Django 5.0.1 on 2024-02-09 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vender', '0011_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_images')),
                ('vender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vender.vendor')),
            ],
        ),
    ]
