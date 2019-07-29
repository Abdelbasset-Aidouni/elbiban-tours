from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,get_user_model
from administration.models import Service,FeedBack,Voyage
from administration.forms import MessageForm
from demand_handler.forms import (
								VisaForm, 
								VisaEtudeForm,
								HotelReservationForm,
								ContratDeTravailForm,
								CreditCardForm,
								ImmigrationForm,
								PlaneTicketForm
								)

User = get_user_model()
def index(request):
	msg_form		= MessageForm(request.POST or None)
	if msg_form.is_valid():
		msg_form.save()
		return HttpResponse(msg_form.cleaned_data.get("content"))

		
	
	voyages			= Voyage.objects.all()
	voyages_1		= voyages[:4]
	voyages_2		= voyages[4:]
	feedbacks 		= FeedBack.objects.all() 
	services 		= Service.objects.all()
	services_1 		= services[:3]
	services_2 		= services[3:]
	context = {
		"services_1":services_1,
		"services_2":services_2,
		"feedbacks":feedbacks,
		"voyages_1":voyages_1,
		"voyages_2":voyages_2


	}
	return render(request,"base.html",context)


def voyage_page(request):
	form 			= PlaneTicketForm(request.POST or None)
	voyages 		= Voyage.objects.all()
	context 		= {
		'voyages':voyages,
		'form':form,
	}
	return render(request,'voyage/voyage.html',context)


def services_page(request):
	services_objects 		= Service.objects.all()
	visa_form 				= VisaForm(request.POST or None)
	visa_etude_form			= VisaEtudeForm(request.POST or None)
	hotel_form				= HotelReservationForm(request.POST or None)
	contrat_travail_form	= ContratDeTravailForm(request.POST or None)
	credit_card_form		= CreditCardForm(request.POST or None)
	immigration_form		= ImmigrationForm(request.POST or None)
	plane_ticket_form		= PlaneTicketForm(request.POST or None)
	services 				= [
		(services_objects[4],visa_form),
		(services_objects[3],visa_etude_form),
		(services_objects[0],hotel_form),
		(services_objects[2],contrat_travail_form),
		(services_objects[1],credit_card_form),
		(services_objects[5],plane_ticket_form),
		(services_objects[6],immigration_form),

	]
	print(services_objects)
	services_without_form	= []
	context 				= {
		"services" : services,
		"services_without_form" : services_without_form,
	}
	print(services_objects[1].get_end_point())

	return render(request,"services/services.html",context)


	