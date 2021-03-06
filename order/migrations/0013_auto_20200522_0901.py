# Generated by Django 2.2.12 on 2020-05-22 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20200519_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderregister',
            name='status',
            field=models.CharField(choices=[('ORDERED', 'ORDERED'), ('APPROVED', 'APPROVED'), ('CONFIRMED', 'CONFIRMED'), ('PACKING', 'PACKING'), ('SHIPPED', 'SHIPPED'), ('RETURNED', 'RETURNED'), ('CLOSED', 'CLOSED'), ('PURCHASED', 'PURCHASED')], default='ORDERED', max_length=20),
        ),
    ]
