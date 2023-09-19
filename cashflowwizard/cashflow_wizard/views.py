from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Reemplaza 'dashboard' con la URL de la página principal de tu aplicación
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
