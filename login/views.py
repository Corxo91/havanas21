from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def welcome_view(request):
    if request.user.is_authenticated:
        return redirect('cocina')
    
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)

from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.if_admin or user.if_comercial or user.if_economica:
                messages.success(request, f'¡Se a autenticado como administrador, {user.username}!')
                return redirect('admin')
            else:
                messages.success(request, f'¡Bienvenido, {user.username}!')
                return redirect('cocina')
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    return redirect('bienvenida')
