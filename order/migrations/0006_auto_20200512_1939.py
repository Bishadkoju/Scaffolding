# Generated by Django 2.2.12 on 2020-05-12 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20200512_1852'),
        ('order', '0005_dncnregister'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderregister',
            name='payment_amount',
        ),
        migrations.AddField(
            model_name='orderregister',
            name='payment_due',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='orderregister',
            name='payment_received',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='orderregister',
            name='payment_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='orderregister',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.ProjectRegister'),
        ),
        migrations.AddField(
            model_name='orderregister',
            name='type',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Rent', 'Rent'), ('Purchase', 'Purchase')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
