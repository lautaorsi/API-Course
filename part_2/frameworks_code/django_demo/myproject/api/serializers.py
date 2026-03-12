from rest_framework import serializers
from .models import Courses

class CourseSerializer(serializers.ModelSerializer):
        class Meta:
                    model = Courses
                    fields = ['course_id', 'subject_code', 'course_title', 'description', 'credits', 'professor_name', 'semester', 'capacity', 'created_at' ]


