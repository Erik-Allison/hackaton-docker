from django import forms

from hospitalApp.models import Especialidades, Medicos, Pacientes, Horarios, Citas


class EspecialidadesForm(forms.ModelForm):
    class Meta:
        model = Especialidades
        fields = '__all__'


class MedicosForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = '__all__'


class PacientesForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'


class HorariosForm(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = '__all__'


class CitasForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = '__all__'
