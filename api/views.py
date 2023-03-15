from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    StudentSerializer,
    StandardSerializer,
    TeacherSerializer,
    SubjectSerializer,
    AttendanceSerializer,
)
from .models import Student, Standard, Teacher, Subject, Attendance
from rest_framework import generics


# Create your views here.
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Student List": "/student-list/",
        "Student Detail View": "/student-detail/<str:pk>/",
        "StandardList": "/standard-list/",
        "Standard Detail View": "/standard-detail/<str:pk>/",
        "Teacher List": "/teacher-list/",
        "Teacher Detail View": "/teacher-detail/<str:pk>/",
        "Subject List": "/subject-list/",
        "Subject Detail View": "/subject-detail/<str:pk>/",
        "Attendance List": "/attendance-list/",
        "Attendance Detail View": "/attendance-detail/<str:pk>/",
    }
    return Response(api_urls)


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StandardList(generics.ListCreateAPIView):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer


class StandardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class AttendanceList(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
