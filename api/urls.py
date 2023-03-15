from django.urls import path
from .views import (
    apiOverview,
    StudentList,
    StudentDetail,
    StandardList,
    StandardDetail,
    TeacherList,
    TeacherDetail,
    SubjectList,
    SubjectDetail,
    AttendanceList,
    AttendanceDetail,
)

urlpatterns = [
    path("", apiOverview, name="api-overview"),
    path("student-list/", StudentList.as_view(), name="student-list"),
    path("student-detail/<str:pk>/", StudentDetail.as_view(), name="student-detail"),
    path("standard-list/", StandardList.as_view(), name="standard-list"),
    path("standard-detail/<str:pk>/", StandardDetail.as_view(), name="standard-detail"),
    path("teacher-list/", TeacherList.as_view(), name="teacher-list"),
    path("teacher-detail/<str:pk>/", TeacherDetail.as_view(), name="teacher-detail"),
    path("subject-list/", SubjectList.as_view(), name="subject-list"),
    path("subject-detail/<str:pk>/", SubjectDetail.as_view(), name="subject-detail"),
    path("attendance-list/", AttendanceList.as_view(), name="attendance-list"),
    path(
        "attendance-detail/<str:pk>/",
        AttendanceDetail.as_view(),
        name="attendance-detail",
    ),
]
