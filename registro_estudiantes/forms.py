from django import forms
from .models import Estudiante


class RegistroEstudianteForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Estudiante
        fields = ['nombre', 'email', 'contraseña']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Estudiante.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email
