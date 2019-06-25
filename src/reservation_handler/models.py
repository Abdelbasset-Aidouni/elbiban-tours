from django.db import models
from elbiban_tours.utilities import upload_image_path
# Create your models here.



class Voyage(models.Model):
	image		= ImageField(upload_to=upload_image_path)
	destination	= CharField(max_length=50)
	price		= DecimalField(max_digits=20,decimal_places=2)
	description	= TextField()
	timestamp	= models.DateField(auto_now_add=False)

