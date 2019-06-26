from django.contrib import admin
from .models import (
				LandingImage,
				GeneralInfo,
				Service,
				FeedBack,
				Voyage
				)


admin.site.register(LandingImage)
admin.site.register(GeneralInfo)
admin.site.register(Service)
admin.site.register(FeedBack)
admin.site.register(Voyage)
