from django import forms
from firstApp.models import Medico
from firstApp.models import Pacientes
from firstApp.models import Cita

class FormMedico(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'
        
class FormPaciente(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'

class FormCita(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'