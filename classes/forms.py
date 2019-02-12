from django import forms
from .models import Classroom, Student, User 


class ClassroomForm(forms.ModelForm):
	class Meta:
		model = Classroom
		fields = '__all__'

class SigninForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email' ,'password']

		widgets={
		'password': forms.PasswordInput(),
		}

class StudentForm(forms.ModelForm):
	class Meta: 
		model = Student
		exclude = ['classroom']     