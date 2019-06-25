from django.contrib import admin
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
admin.site.register(Demand)
admin.site.register(Visa)
admin.site.register(VisaEtude)
admin.site.register(PlaneTicket)
admin.site.register(Hebergement)
admin.site.register(Immigration)
admin.site.register(CreditCard)
admin.site.register(ContratDeTravail)
admin.site.register(HotelReservation)
admin.site.register(Requirement)
