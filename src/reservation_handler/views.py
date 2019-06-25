from django.shortcuts import render,redirect,get_object_or_404
from .models import Voyage
# Create your views here.
def reserve_voyage(request,pk):
	voyage = get_object_or_404(Voyage,pk==pk)
	