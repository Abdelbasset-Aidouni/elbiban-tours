# Generated by Django 2.2.2 on 2019-07-26 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand_handler', '0009_auto_20190626_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='demande',
            field=models.CharField(choices=[('cc', 'Credit Card'), ('imgr', 'Immigration'), ('hbrg', 'Hébergement'), ('vs', 'visa'), ('ct', 'Contrat De Travail'), ('hr', 'Réservation Hotel'), ('pt', "Billet D'avion"), ('vse', "Visa d'étude")], default='vs', max_length=15),
        ),
    ]