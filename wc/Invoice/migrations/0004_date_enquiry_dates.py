# Generated by Django 5.0.1 on 2024-03-16 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0003_remove_enquiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='enquiry',
            name='dates',
            field=models.ManyToManyField(related_name='enquiries_dates', to='Invoice.date'),
        ),
    ]
