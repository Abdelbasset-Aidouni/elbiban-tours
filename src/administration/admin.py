from django.contrib import admin
from .models import (
				LandingImage,
				GeneralInfo,
				Service,
				FeedBack,
				Voyage,
				
				Message,
				Requirement,
				NewsLetter,
				NewsLetterMember
				)


admin.site.register(LandingImage)
admin.site.register(GeneralInfo)
admin.site.register(Service)
admin.site.register(FeedBack)
admin.site.register(Voyage)


admin.site.register(Message)
admin.site.register(Requirement)
admin.site.register(NewsLetter)
admin.site.register(NewsLetterMember)