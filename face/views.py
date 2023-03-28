# Path: face/views.py
# Description: This file contains the views for the face app.

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from deepface import DeepFace
from rest_framework import generics, mixins
from rest_framework.views import APIView
from retinaface import RetinaFace
import sqlite3
from PIL import Image

from face.serializers import FaceSerializer
# serializers
# models


# Create your views here.
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "embed face": "/embed/",
        "detect face": "/detect/",
        "recognise face": "/recognise/",
        "count faces": "/count/",
    }
    return Response(api_urls)

class EmbedFace(generics.GenericAPIView):
    # serializer_class = FaceSerializer

    def post(self, request, *args, **kwargs):
        image = request.data["faceImg"]
        embedding = DeepFace.represent(image, model_name="Facenet")
        return Response(embedding)


class DetectFace(generics.GenericAPIView):
    # serializer_class = FaceSerializer

    def post(self, request, *args, **kwargs):
        image = request.data["faceImg"]
        detection = RetinaFace.detect_faces(image)
        return Response(detection)

class RecogniseFace(generics.GenericAPIView):
    # serializer_class = FaceSerializer
    def post(self, request, *args, **kwargs):
        image = request.data["faceImg"]
        # try:
        #     db = sqlite3.connect("db.sqlite3")
        #     cursor = db.cursor()
        #     cursor.execute("SELECT * FROM api_student")
        #     dbimgs = cursor.fetchall()
        #     identity = list()
        #     for dbimg in dbimgs:
        #         name = dbimg[2]
        #         img = dbimg[7]
        # except sqlite3.Error as error:
        #     print(format(error))

        # finally:
        #     if db:
        #         db.close()
        identity = DeepFace.find(img_path=image,db_path="/home/lox/projects/mainProject/database",model_name="Facenet")
        return Response(identity)

class CountFaces(generics.GenericAPIView):
    # serializer_class = FaceSerializer
    def post(self, request, *args, **kwargs):
        image = request.data["faceImg"]
        faces = RetinaFace.detect_faces(image)
        return Response(len(faces))