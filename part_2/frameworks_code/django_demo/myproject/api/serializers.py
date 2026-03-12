from rest_framework import serializers
from .models import Courses

# Serializador de curso
class CourseSerializer(serializers.ModelSerializer):
        class Meta:
                    model = Courses
                    fields = ['course_id', 'course_title', 'credits']


