# Generated by Django 2.2.2 on 2019-06-29 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_auto_20190629_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyage',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
