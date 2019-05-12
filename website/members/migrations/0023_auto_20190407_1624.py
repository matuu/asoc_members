# Generated by Django 2.0.4 on 2019-04-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0022_payment_invoice_ok'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='invoice_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de factura'),
        ),
        migrations.AddField(
            model_name='payment',
            name='invoice_spoint',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Punto de venta'),
        ),
        migrations.RemoveField(
            model_name='payment',
            name='invoice_id',
        ),
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together={('invoice_spoint', 'invoice_number')},
        ),
    ]
