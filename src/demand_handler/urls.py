from django.urls import path
from .views import (
			visa_demand,
			visa_etude_demand,
			contrat_travail_demand,
			hotel_reservation_demand,
			immigration_demand,
			credit_card_demand,
			plane_ticket_demand
			)

urlpatterns = [
	path('visa/', visa_demand),
	path('visa-etude/', visa_etude_demand),
	path('contrat-de-travail/', contrat_travail_demand),
	path('hotel-reservation/', hotel_reservation_demand),
	path('immigration/', immigration_demand),
	path('plane-ticket/', plane_ticket_demand),
	path('credit-card/', credit_card_demand),
	
    
]