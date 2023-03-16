# Path: api/serializers.py
# Description: This file contains the serializers for the api app.

from rest_framework.serializers import ModelSerializer
from .models import Student, Standard, Teacher, Subject, Attendance

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StandardSerializer(ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class AttendanceSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

