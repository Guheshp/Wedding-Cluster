# Generated by Django 5.0.1 on 2024-03-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0020_invoice_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicehistory',
            name='invoice_number',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
