from django.contrib import admin
from .models import Doctor, AppoinmentPatient
# Register your models here.
admin.site.register(Doctor)
admin.site.register(AppoinmentPatient)