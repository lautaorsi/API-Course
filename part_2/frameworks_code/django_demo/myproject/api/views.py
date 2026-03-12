from django.shortcuts import render
from rest_framework import viewsets 
from .models import Courses
from .serializers import CourseSerializer  


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer