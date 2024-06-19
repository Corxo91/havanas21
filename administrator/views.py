from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import cocina.urls

@login_required
def admin(request):
    return render(request, 'administrador.html')

