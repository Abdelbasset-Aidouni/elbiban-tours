# Generated by Django 2.2.2 on 2019-07-01 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_auto_20190629_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voyage',
            name='description',
        ),
        migrations.AddField(
            model_name='voyage',
            name='availability',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('non disponible', 'non disponible')], default='Disponible', max_length=20),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='client_badge',
            field=models.CharField(choices=[('nouveau client', 'nouveau client'), ('client fidèle', 'client fidèle')], default='nouveau client', max_length=20),
        ),
    ]
