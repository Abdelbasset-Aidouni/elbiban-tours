# Generated by Django 2.2.2 on 2019-08-03 18:30

from django.db import migrations, models
import elbiban_tours.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0025_auto_20190803_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModelKhra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=elbiban_tours.utilities.upload_image_path)),
            ],
        ),
    ]
