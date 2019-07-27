from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,get_user_model
from administration.models import Service,FeedBack,Voyage
from administration.forms import MessageForm
from demand_handler.forms import PlaneTicketForm
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