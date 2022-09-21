from pyexpat import model
from rest_framework import serializers
from .models import Doctor, Appoinment_Patient

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class  AppoinmentPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Appoinment_Patient
        fields = "__all__"