from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import PlaneTicket
from time import sleep
from administration.models import Voyage
from .forms import (
				VisaForm, 
				VisaEtudeForm,
				HotelReservationForm,
				ContratDeTravailForm,
				CreditCardForm,
				ImmigrationForm,
				PlaneTicketForm
				)



def visa_demand(request,pk=None):
	form = VisaForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form.save()
		print("saved successfuly")

	else:
		print(form)
		print("fail")
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





def plane_ticket_demand(request,pk=None):
	form = PlaneTicketForm(request.POST or None)

	if form.is_valid():
		
		form_data = form.cleaned_data
		obj = PlaneTicket(
				first_name=form_data.get("first_name"),
				last_name=form_data.get("last_name"),
				phone_number=form_data.get("phone_number"),
				destination=get_object_or_404(Voyage,pk=pk)
			)
		obj.save()
		return JsonResponse({},status=200)
	else:
		return JsonResponse({},status=400)
	
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

