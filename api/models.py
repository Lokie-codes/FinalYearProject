from django.db import models

class Student(models.Model):
	rollNo = models.IntegerField()
	name = models.CharField(max_length=100)
	gender = models.CharField(max_length=10)
	faceId = models.CharField(max_length=200)
	address = models.CharField(max_length=500)
	standardId = models.ForeignKey("Standard", verbose_name=("standardId"), on_delete=models.CASCADE)
	slug = models.SlugField()

	def __str__(self):
		return f'{self.name} {self.gender} {self.address}'

	def get_absolute_url(self):
		return f'/{self.slug}/'
	
	class Meta:
		ordering = ('rollNo',)

class Standard(models.Model):
	standardId = models.IntegerField()
	name = models.CharField(max_length=20)
	section = models.CharField(max_length=50)
	slug = models.SlugField()

	def __str__(self) -> str:
		return f'{self.name} {self.section}'
	
	def get_absolute_url(self):
		return f'/{self.slug}/'
	
	class Meta:
		ordering = ('standardId',)

class Teacher(models.Model):
	teacherId = models.CharField(max_length=100)
	name = models.CharField(max_length=150)
	email = models.EmailField()
	password = models.CharField(max_length=150)
	phone = models.BigIntegerField()

	def __str__(self) -> str:
		return f'{self.name} {self.email} {self.phone}'
	
	def get_absolute_url(self):
		return f'/{self.slug}/'
	
	class Meta:
		ordering = ('teacherId',)

class Subject(models.Model):
	subjectId = models.IntegerField()
	name = models.CharField(max_length=150)

	def __str__(self) -> str:
		return f'{self.subjectId} {self.name}'
	
	def get_absolute_url(self):
		return f'/{self.slug}/'
	
	class Meta:
		ordering = ('subjectId',)

class Attendance(models.Model):
	classId = models.ForeignKey("Standard", verbose_name=("standardId"), on_delete=models.CASCADE)
	studentId = models.ForeignKey("Student", verbose_name=("rollNo"), on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	time = models.DateField(auto_now=True)
	subjectId = models.ForeignKey("Subject", verbose_name=('subjectId'), on_delete=models.CASCADE)
	slug = models.SlugField()
	isPresent = models.BooleanField(default=True)

	def __str__(self) -> str:
		return f'{self.date} {self.time} {self.subjectId} {self.studentId} {self.isPresent}'
	
	def get_absolute_url(self):
		return f'/{self.slug}/'
	
	class Meta:
		ordering = ('classId',)