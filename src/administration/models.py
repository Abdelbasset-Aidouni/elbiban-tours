from django.db import models
from elbiban_tours.utilities import upload_image_path
from django.contrib.auth import get_user_model

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
	svg				= models.FileField(upload_to=upload_image_path,null=True)


class FeedBack(models.Model):
	CLIENT_FIDELE = 'client fidèle'
	CLIENT_NEW	  = 'nouveau client'
	CLIENT_CHOICES = {
		(CLIENT_FIDELE,'client fidèle'),
		(CLIENT_NEW,'nouveau client')
	}
	user  			= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	image 			= models.ImageField(upload_to=upload_image_path)
	username		= models.CharField(max_length=50,blank=True,null=True)
	client_badge	= models.CharField(max_length=20,choices=CLIENT_CHOICES,default=CLIENT_NEW)
	feedback 		= models.TextField()


class Voyage(models.Model):
	image		= models.ImageField(upload_to=upload_image_path)
	destination	= models.CharField(max_length=50)
	price		= models.DecimalField(max_digits=20,decimal_places=2)
	description	= models.TextField()
	timestamp	= models.DateField(auto_now_add=False)

class ReservationVisa(models.Model):
	destination		= models.CharField(max_length=50)
	description 	= models.TextField()
	price			= models.DecimalField(max_digits=10,decimal_places=2)
	date 			= models.DateField(blank=True,null=True)

class VisaEtudeReservation(ReservationVisa):
	country			= models.CharField(max_length=50)
	Universty		= models.CharField(max_length=50)
