from django import forms
from .models import (
				Demand, 
				Visa,
				VisaEtude, 
				PlaneTicket,
				Hebergement,
				Immigration,
				CreditCard,
				ContratDeTravail,
				HotelReservation,
				Requirement
				)
class DemandForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = ('first_name','last_name','phone_number')


class VisaForm(DemandForm):
	class Meta:
		model = Visa
		fields =  ('passport','first_name','last_name','phone_number') 

class VisaEtudeForm(VisaForm):
	class Meta:
		model = VisaEtude
		fields = VisaForm.Meta.fields + ('country',) 

class CreditCardForm(DemandForm):
	class Meta:
		model = CreditCard
		fields = DemandForm.Meta.fields + ('passport','designation') 


class ImmigrationForm(DemandForm):
	class Meta:
		model = Immigration
		fields = DemandForm.Meta.fields + ('country',) 


class PlaneTicketForm(DemandForm):
	class Meta:
		model = PlaneTicket
		fields = DemandForm.Meta.fields


class ContratDeTravailForm(DemandForm):
	class Meta:
		model = ContratDeTravail
		fields = DemandForm.Meta.fields 

class HotelReservationForm(DemandForm):
	class Meta:
		model = HotelReservation
		fields = DemandForm.Meta.fields + ('location',) 