# Generated by Django 5.0.1 on 2024-02-14 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vender', '0014_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='service_images')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='vender.service')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vender.vendor')),
            ],
        ),
    ]
