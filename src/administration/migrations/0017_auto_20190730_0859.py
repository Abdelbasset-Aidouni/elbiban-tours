# Generated by Django 2.2.2 on 2019-07-30 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0016_service_is_in_section_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='form',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='client_badge',
            field=models.CharField(choices=[('client fidèle', 'client fidèle'), ('nouveau client', 'nouveau client')], default='nouveau client', max_length=20),
        ),
    ]