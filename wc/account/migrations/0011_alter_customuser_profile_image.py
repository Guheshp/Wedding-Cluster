# Generated by Django 5.0.1 on 2024-02-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_Image',
            field=models.ImageField(blank=True, default='userdefaultimg.png', null=True, upload_to='profile_img'),
        ),
    ]
