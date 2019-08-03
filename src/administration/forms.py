from django import forms
from .models import Message,NewsLetterMember

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('__all__')
		labels = {
			"first_name"	: 'Nom',
			"last_name"		: 'Prénom',
			"phone_number"	: 'Numéro Téléphone',
			"content"		: 'Contenue',
		}

class NewsLetterForm(forms.ModelForm):
	class Meta:
		model = NewsLetterMember
		fields = ('email',)