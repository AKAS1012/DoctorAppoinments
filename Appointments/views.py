from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Doctor, Appoinment_Patient
from .serializers import DoctorSerializer, AppoinmentPatientSerializer

# Create your views here.
class DoctorList(APIView):
    def get(self, request, format=None):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientAppointmentList(APIView):
    def get(self, request, format=None):
        patients = Appoinment_Patient.objects.all()
        serializer = AppoinmentPatientSerializer(patients, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = Appoinment_Patient(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
