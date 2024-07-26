from django.shortcuts import render, redirect
<<<<<<< HEAD
from administrator.models import Receta

def bar(request):
    barEp = Receta.objects.filter(active="Sí", place="Bar", category="Cafés").order_by('recipe')
    barEf = Receta.objects.filter(active="Sí", place="Bar", category="Bebidas").order_by('recipe')
    context = {
        'barEp': barEp,
        'barEf': barEf,
    }
    return render(request, 'cafe.html', context)

def salon(request):
    salonEP = Receta.objects.filter(active="Sí", place="Restaurante", category="Entre Panes").order_by('recipe')
    salonEF = Receta.objects.filter(active="Sí", place="Restaurante", category="Entrantes Fríos").order_by('recipe')
    salonEC = Receta.objects.filter(active="Sí", place="Restaurante", category="Entrantes Calientes").order_by('recipe')
    salonCI = Receta.objects.filter(active="Sí", place="Restaurante", category="Cocina Italiana").order_by('recipe')
    salonPF = Receta.objects.filter(active="Sí", place="Restaurante", category="Platos Fuertes").order_by('recipe')
    salonG = Receta.objects.filter(active="Sí", place="Restaurante", category="Guarniciones").order_by('recipe')
    salonP = Receta.objects.filter(active="Sí", place="Restaurante", category="Postres").order_by('recipe')
    
    context = {
        'salonEP': salonEP,
        'salonEF': salonEF,
        'salonEC': salonEC,
        'salonCI': salonCI,
        'salonPF': salonPF,
        'salonG': salonG,
        'salonP': salonP,
    }
    return render(request, 'salon.html', context)
=======

def bar(request):
    return render(request, 'cafe.html')

def salon(request):
    return render(request, 'salon.html')
>>>>>>> 800db762a542d7ba1511d3ceaf6b32a37e3cc2ec
