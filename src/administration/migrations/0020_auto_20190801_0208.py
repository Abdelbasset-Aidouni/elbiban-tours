# Generated by Django 2.2.2 on 2019-08-01 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0019_auto_20190731_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='agency_detailed_desc',
            field=models.TextField(default='frghana'),
        ),
        migrations.AddField(
            model_name='service',
            name='is_on_about',
            field=models.BooleanField(default=False),
        ),
    ]
