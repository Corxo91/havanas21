from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def cocina(request):
    return render(request, 'tools.html', {})

def logout_view(request):
    logout(request)
    return redirect('bienvenida')