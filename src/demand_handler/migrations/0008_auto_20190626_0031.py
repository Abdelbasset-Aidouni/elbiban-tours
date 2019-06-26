# Generated by Django 2.2.2 on 2019-06-25 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demand_handler', '0007_auto_20190625_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planeticket',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administration.Voyage'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='demande',
            field=models.CharField(choices=[('ct', 'Contrat De Travail'), ('vs', 'visa'), ('hbrg', 'Hébergement'), ('imgr', 'Immigration'), ('hr', 'Réservation Hotel'), ('pt', "Billet D'avion"), ('vse', "Visa d'étude"), ('cc', 'Credit Card')], default='vs', max_length=15),
        ),
    ]