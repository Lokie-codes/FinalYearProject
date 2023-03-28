# Path: face/models.py
# Description: This file contains the models for the face app.

from django.db import models

# Create your models here.
# class Face(models.Model):
#     faceImg = models.ImageField(null=True, blank=True, upload_to="database/")
#     embedding = models.TextField(null=True, blank=True)
#     studentId = models.ForeignKey("api.Student", verbose_name=("studentId"), on_delete=models.CASCADE)
#     slug = models.SlugField(null=True, blank=True)

#     def __str__(self):
#         return f'{self.studentId}'
    
#     def get_absolute_url(self):
#         return f'/{self.slug}/'
    