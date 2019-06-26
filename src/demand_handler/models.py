from django.db import models
from django.contrib.auth import get_user_model
from elbiban_tours.utilities import upload_image_path
from administration.models import Voyage,visaReservation,VisaEtudeReservation
User = get_user_model()

class Demand(models.Model):
	user 			= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	slug 			= models.SlugField(max_length=50,blank=True)
	first_name 		= models.CharField(max_length=50,blank=True,default="khra")
	last_name 		= models.CharField(max_length=50)
	phone_number 	= models.CharField(max_length=50,blank=True)
	timestamp		= models.DateField(auto_now_add=True)


class Visa(Demand):
	designated_visa = models.ForeignKey(VisaReservation,on_delete=models.SET_NULL,null=True)
	passport 		= models.ImageField(upload_to=upload_image_path,blank=True,null=True)

class VisaEtude(Visa):
	designated_visa = models.ForeignKey(VisaEtudeReservation,on_delete=models.SET_NULL,null=True)
	country 		= models.CharField(max_length=50,default="spain")

class Hebergement(Demand):
	country 		= models.CharField(max_length=50,default="Canada")

class Immigration(Demand):
	country 		= models.CharField(max_length=50,default="Canada")

class CreditCard(Demand):
	MASTER_CARD = 'mc'
	VISA_CARD	= 'vc'
	CREDIT_CARD_CHOICES = {
		(MASTER_CARD,'Master Card'),
		(VISA_CARD,'Visa Card')
	}
	designation 	= models.CharField(max_length=20,choices=CREDIT_CARD_CHOICES,default=VISA_CARD)
	passport		= models.ImageField(upload_to=upload_image_path)	

class ContratDeTravail(Demand):
	pass


class PlaneTicket(Demand):
	destination 		= models.ForeignKey(Voyage,on_delete=models.CASCADE,null=True)

class HotelReservation(Demand):
	location 			= models.CharField(max_length=50)

	

class Requirement(models.Model):
	designation 		= models.CharField(max_length=100)
	VISA 				= 'vs'
	VISA_ETUDE			= 'vse'
	IMMIGRATION 		= 'imgr'
	HEBERGEMENT 		= 'hbrg'
	CREDIT_CARD 		= 'cc'
	CONTRAT_TRAVAIL		= 'ct'
	PLANE_TICKET		= 'pt'
	HOTEL_RESERVATION	= 'hr'
	DEMAND_CHOICES		= {
	(VISA,"visa"),
	(VISA_ETUDE,"Visa d'étude"),
	(IMMIGRATION,"Immigration"),
	(HEBERGEMENT,"Hébergement"),
	(CREDIT_CARD,"Credit Card"),
	(CONTRAT_TRAVAIL,"Contrat De Travail"),
	(PLANE_TICKET,"Billet D'avion"),
	(HOTEL_RESERVATION,"Réservation Hotel"),
	}
	demande 			= models.CharField(max_length=15,choices=DEMAND_CHOICES,default=VISA)