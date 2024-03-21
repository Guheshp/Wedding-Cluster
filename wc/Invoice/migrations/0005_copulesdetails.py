# Generated by Django 5.0.1 on 2024-03-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0004_date_enquiry_dates'),
    ]

    operations = [
        migrations.CreateModel(
            name='CopulesDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groomname', models.CharField(max_length=255)),
                ('groomDOB', models.DateField(null=True)),
                ('groomfathername', models.CharField(max_length=255)),
                ('groommothername', models.CharField(max_length=255)),
                ('groom_proof_image', models.ImageField(upload_to='groom_proof_images')),
                ('bridename', models.CharField(max_length=255)),
                ('brideDOB', models.DateField(null=True)),
                ('bridfathername', models.CharField(max_length=255)),
                ('bridmothername', models.CharField(max_length=255)),
                ('brid_proof_image', models.ImageField(upload_to='brid_proof_images')),
                ('advance_amt', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CopulesDetails',
                'verbose_name_plural': 'CopulesDetails',
            },
        ),
    ]