# Generated by Django 5.0.1 on 2024-03-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0011_remove_invoice_customer_delete_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copulesdetails',
            name='advance_amt',
        ),
        migrations.RemoveField(
            model_name='copulesdetails',
            name='advance_paid_date',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='pay_amt',
        ),
        migrations.AddField(
            model_name='invoice',
            name='advance_amt',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='advance_paid_date',
            field=models.DateField(null=True),
        ),
    ]
