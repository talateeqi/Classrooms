from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

gender_choices = {
('M', 'MALE'),
('F', 'FEMALE'),
}

class Student(models.Model):
	name = models.CharField(max_length=120)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=50, choices=gender_choices)
	exam_grade = models.DecimalField(max_digits=7, decimal_places=3)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, default=1)