# Generated by Django 2.2.2 on 2019-06-29 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_auto_20190629_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='client_badge',
            field=models.CharField(choices=[('client fidèle', 'client fidèle'), ('nouveau client', 'nouveau client')], default='nouveau client', max_length=20),
        ),
        migrations.AlterField(
            model_name='voyage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voyage',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]