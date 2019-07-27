from django.db import models
from elbiban_tours.utilities import upload_image_path
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class LandingImage(models.Model):
	image 		= models.ImageField(upload_to=upload_image_path)
	active		=models.BooleanField(default=False)


class GeneralInfo(models.Model):
	landing_title_1 		= models.CharField(max_length=50)
	landing_title_2 		= models.CharField(max_length=50)
	phone_number			= models.DecimalField(max_digits=10,decimal_places=0)
	fax_number				= models.DecimalField(max_digits=9,decimal_places=0)
	email 					= models.EmailField()
	agency_description		= models.TextField()
	location 				= models.CharField(max_length=100)
	facebook_link			= models.CharField(max_length=100)
	twitter_link			= models.CharField(max_length=100)
	instagram_link			= models.CharField(max_length=100)
	msg_confirmation		= models.CharField(max_length=250)





class Service(models.Model):
	designation		= models.CharField(max_length=50)
	description		= models.TextField()
	is_in_landing	= models.BooleanField(default=False)
	svg				= models.FileField(upload_to=upload_image_path,null=True)

	def __str__(self):
		return self.designation


class FeedBack(models.Model):
	CLIENT_FIDELE = 'client fidèle'
	CLIENT_NEW	  = 'nouveau client'
	CLIENT_CHOICES = {
		(CLIENT_FIDELE,'client fidèle'),
		(CLIENT_NEW,'nouveau client')
	}
	user  			= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	image 			= models.ImageField(upload_to=upload_image_path)
	username		= models.CharField(max_length=50,blank=True,null=True)
	client_badge	= models.CharField(max_length=20,choices=CLIENT_CHOICES,default=CLIENT_NEW)
	feedback 		= models.TextField()
	def __str__(self):
		return self.username


class Voyage(models.Model):
	AVAILABLE	= 'Disponible'
	NOT_AVAILABLE 	= 'indisponible'
	AVAILABILITY 	= {
	(AVAILABLE,'disponible'),
	(NOT_AVAILABLE,'indisponible')
	}
	image		= models.ImageField(upload_to=upload_image_path)
	destination	= models.CharField(max_length=50)
	price		= models.DecimalField(max_digits=20,decimal_places=0)
	availability= models.CharField(max_length=20,choices=AVAILABILITY,default=AVAILABLE)
	timestamp	= models.DateField(auto_now_add=False)
	best		= models.BooleanField(default=False)

	def __str__(self):
		return self.destination

	def get_end_point(self):
		return reverse("plane_ticket_demand",kwargs={"pk":self.pk})

class ReservationVisa(models.Model):
	destination		= models.CharField(max_length=50)
	description 	= models.TextField()
	price			= models.DecimalField(max_digits=10,decimal_places=2)
	date 			= models.DateField(blank=True,null=True)
	def __str__(self):
		return "{}{}".format(self.destination,date)

class VisaEtudeReservation(ReservationVisa):
	country			= models.CharField(max_length=50)
	Universty		= models.CharField(max_length=50)


class Message(models.Model):
	first_name		= models.CharField(max_length=20)
	last_name		= models.CharField(max_length=20)
	phone_number 	= models.DecimalField(max_digits=10,decimal_places=0)
	email 			= models.EmailField()
	content 		= models.TextField()
	def __str__(self):
		return "{} {}".format(self.first_name,self.last_name)