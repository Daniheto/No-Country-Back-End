from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import RegistroEstudianteForm

# Create your views here.


def registro_estudiante(request):
    if request.method == 'POST':
        form = RegistroEstudianteForm(request.POST)
        if form.is_valid():
            # Guarda el estudiante
            estudiante = form.save(commit=False)
            # Aquí puedes encriptar la contraseña
            estudiante.contraseña = make_password(
                form.cleaned_data['contraseña'])
            estudiante.save()
            return redirect('login')  # Redirigir a la página de login
    else:
        form = RegistroEstudianteForm()

    return render(request, 'registro.html', {'form': form})
