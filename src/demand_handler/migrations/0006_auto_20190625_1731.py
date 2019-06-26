# Generated by Django 2.2.2 on 2019-06-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand_handler', '0005_auto_20190625_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='designation',
            field=models.CharField(choices=[('mc', 'Master Card'), ('vc', 'Visa Card')], default='vc', max_length=20),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='demande',
            field=models.CharField(choices=[('hbrg', 'Hébergement'), ('vs', 'visa'), ('cc', 'Credit Card'), ('ct', 'Contrat De Travail'), ('pt', "Billet D'avion"), ('imgr', 'Immigration'), ('hr', 'Réservation Hotel'), ('vse', "Visa d'étude")], default='vs', max_length=15),
        ),
    ]