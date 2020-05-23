# Generated by Django 2.2.12 on 2020-05-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItemsRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_register', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_rate', models.DecimalField(decimal_places=4, default=0.0, max_digits=5)),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('payment_advance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='ORDERED', max_length=20)),
            ],
        ),
    ]