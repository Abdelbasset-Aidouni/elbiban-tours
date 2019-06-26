# Generated by Django 2.2.2 on 2019-06-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand_handler', '0004_auto_20190625_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='designation',
            field=models.CharField(choices=[('vc', 'Visa Card'), ('mc', 'Master Card')], default='vc', max_length=20),
        ),
        migrations.AlterField(
            model_name='planeticket',
            name='destination',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='demande',
            field=models.CharField(choices=[('imgr', 'Immigration'), ('cc', 'Credit Card'), ('pt', "Billet D'avion"), ('vse', "Visa d'étude"), ('hr', 'Réservation Hotel'), ('hbrg', 'Hébergement'), ('vs', 'visa'), ('ct', 'Contrat De Travail')], default='vs', max_length=15),
        ),
    ]