from django.shortcuts import render
from .forms import (
				VisaForm, 
				VisaEtudeForm,
				HotelReservationForm,
				ContratDeTravailForm,
				CreditCardForm,
				ImmigrationForm,
				PlaneTicketForm
				)



def visa_demand(request):
	form = VisaForm(request.POST or None)
	if form.is_valid():
		form.save()

	context = {
		"form":form
	}
	return render(request,'test.html',context)



def visa_etude_demand(request):
	form = VisaEtudeForm(request.POST or None)
	if form.is_valid():
		form.save()
	
	context = {
		"form":form
	}
	return render(request,'test.html',context)




def credit_card_demand(request):
	form = CreditCardForm(request.POST or None)
	if form.is_valid():
		form.save()
	
	context = {
		"form":form
	}
	return render(request,'test.html',context)



def immigration_demand(request):
	form = ImmigrationForm(request.POST or None)
	if form.is_valid():
		form.save()
	
	context = {
		"form":form
	}
	return render(request,'test.html',context)



def plane_ticket_demand(request):
	form = PlaneTicketForm(request.POST or None)
	if form.is_valid():
		form.save()
	
	context = {
		"form":form
	}
	return render(request,'test.html',context)

def contrat_travail_demand(request):
	form = ContratDeTravailForm(request.POST or None)
	if form.is_valid():
		form.save()
	
	context = {
		"form":form
	}
	return render(request,'test.html',context)

def hotel_reservation_demand(request):
	form = HotelReservationForm(request.POST or None)
	if form.is_valid():
		form.save()
	
	context = {
		"form":form
	}
	return render(request,'test.html',context)



def send_demand(request):
	pass

