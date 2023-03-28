# Path: face/urls.py
# Description: This file contains the urls for face app

from django.urls import path
from .views import EmbedFace, DetectFace, RecogniseFace, CountFaces, apiOverview

urlpatterns = [
    path("",apiOverview, name="api-overview"),
    path("embed/", EmbedFace.as_view(), name="embed-face"),
    path("detect/", DetectFace.as_view(), name="detect-face"),
    path("recognise/", RecogniseFace.as_view(), name="recognise-face"),
    path("count/", CountFaces.as_view(), name="count-faces"),
]