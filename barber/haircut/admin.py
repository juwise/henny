from django.contrib import admin
from .models import Contact, Haircut


admin.site.register(Contact)
admin.site.register(Haircut)
admin.site.site_header = "Administration"
