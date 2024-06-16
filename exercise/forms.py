from django.forms import ModelForm

from .models import Exercise


class ExerciseForm(ModelForm):
  class Meta:
    model = Exercise
    fields = '__all__'
    labels = {
      'name': 'Nombre',
      'description': 'Descripción',
      'input_description': 'Entrada esperada',
      'output_description': 'Salida esperada',
      'start_date': 'Fecha de inicio',
      'end_date': 'Fecha de cierre'
    }
