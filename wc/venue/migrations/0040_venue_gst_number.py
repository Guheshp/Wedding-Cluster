# Generated by Django 5.0.1 on 2024-03-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0039_restrictions_user_restrictions_venue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='gst_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]