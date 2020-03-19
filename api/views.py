from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from api.serializers import StudentSerializer
from api.models import Student

# Create your views here.

class StudentCreateAPIView(ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    