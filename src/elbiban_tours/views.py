from django.shortcuts import render
from django.contrib.auth import authenticate, login,get_user_model

User = get_user_model()
def index(request):
	
	context = {

	}
	return render(request,"base.html",context)