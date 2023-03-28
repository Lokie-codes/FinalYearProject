# Path: api/admin.py
# Description: This file contains the admin for the api app.

from django.contrib import admin
from .models import Student, Standard, Teacher, Subject, Attendance
from face.models import Face

# Register your models here.
admin.site.register(Student)
admin.site.register(Standard)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Attendance)

admin.site.register(Face)
