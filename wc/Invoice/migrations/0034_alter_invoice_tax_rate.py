# Generated by Django 5.0.1 on 2024-03-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0033_remove_invoicehistory_tax_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='tax_rate',
            field=models.FloatField(null=True),
        ),
    ]