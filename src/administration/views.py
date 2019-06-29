from django.shortcuts import render
from .forms import MessageForm

def message_handler(request):
	form 		= MessageForm(request.POST)
	context 	= {
		"msg_form":form
	}
	return render(request,"test.html",context)

