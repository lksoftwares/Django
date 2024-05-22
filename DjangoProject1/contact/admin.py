from django.contrib import admin
from contact.models import contactModel
class contactAdmin(admin.ModelAdmin):
          list_display=('Name','Contact_No','email','Address')
admin.site.register(contactModel,contactAdmin)          
