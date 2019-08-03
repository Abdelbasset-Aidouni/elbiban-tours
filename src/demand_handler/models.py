from django.db import models
from django.contrib.auth import get_user_model
from elbiban_tours.utilities import upload_image_path
from administration.models import Voyage
User = get_user_model()

class Demand(models.Model):
	user 			= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	slug 			= models.SlugField(max_length=50,blank=True)
	first_name 		= models.CharField(max_length=50,blank=True)
	last_name 		= models.CharField(max_length=50)
	phone_number 	= models.DecimalField(max_digits=10,decimal_places=0)
	timestamp		= models.DateField(auto_now_add=True)

	def __str__(self):
		return "{} {}".format(self.first_name,self.last_name)


class Visa(Demand):
	destination		= models.CharField(max_length=50,default="france")
	passport 		= models.ImageField(upload_to=upload_image_path,blank=True,null=True)

class VisaEtude(Visa):
	
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

	

