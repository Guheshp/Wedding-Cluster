# Generated by Django 5.0.1 on 2024-03-27 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0029_enquiry_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='tax_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='invoicehistory',
            name='tax_rate',
            field=models.IntegerField(null=True),
        ),
    ]
