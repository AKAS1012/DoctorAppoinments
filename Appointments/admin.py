from django.contrib import admin
from .models import Doctor, Appoinment_Patient
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Appoinment_Patient)