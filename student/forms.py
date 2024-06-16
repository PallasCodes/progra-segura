from django.forms import ModelForm

from .models import Student
from django.contrib.auth.models import User


class StudentForm(ModelForm):
  class Meta:
    model = Student
    fields = ['registration_number', 'full_name']
    labels = {
      'registration_number': 'Matricula',
      'full_name': 'Nombre completo'
    }


class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password', ]
    labels = {
      'username': 'Nombre de usuario',
      'password': 'Contraseña',
      'email': 'Email'
    }