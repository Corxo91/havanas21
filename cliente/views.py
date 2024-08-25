from django.shortcuts import render
from administrator.models import Receta


def bar(request):
    barEp = Receta.objects.filter(active="Sí", place="Bar", category="Cafés").order_by('recipe').prefetch_related('galery_client').all()
    barEf = Receta.objects.filter(active="Sí", place="Bar", category="Bebidas").order_by('recipe').prefetch_related('galery_client').all()
    barS = Receta.objects.filter(active="Sí", place="Bar", category="Sugerencias").order_by('recipe').prefetch_related('galery_client').all()
    
    context = {
        'barEp': barEp,
        'barEf': barEf,
        'barS': barS,
    }
    return render(request, 'cafe.html', context)

def salon(request):
    salonEP = Receta.objects.filter(active="Sí", place="Restaurante", category="Entre Panes").order_by('recipe').prefetch_related('galery_client').all()
    salonEF = Receta.objects.filter(active="Sí", place="Restaurante", category="Entrantes Fríos").order_by('recipe').prefetch_related('galery_client').all()
    salonEC = Receta.objects.filter(active="Sí", place="Restaurante", category="Entrantes Calientes").order_by('recipe').prefetch_related('galery_client').all()
    salonCI = Receta.objects.filter(active="Sí", place="Restaurante", category="Cocina Italiana").order_by('recipe').prefetch_related('galery_client').all()
    salonPF = Receta.objects.filter(active="Sí", place="Restaurante", category="Platos Fuertes").order_by('recipe').prefetch_related('galery_client').all()
    salonG = Receta.objects.filter(active="Sí", place="Restaurante", category="Guarniciones").order_by('recipe').prefetch_related('galery_client').all()
    salonP = Receta.objects.filter(active="Sí", place="Restaurante", category="Postres").order_by('recipe').prefetch_related('galery_client').all()
    salonS = Receta.objects.filter(active="Sí", place="Restaurante", category="Sugerencias").order_by('recipe').prefetch_related('galery_client').all()
    
    context = {
        'salonEP': salonEP,
        'salonEF': salonEF,
        'salonEC': salonEC,
        'salonCI': salonCI,
        'salonPF': salonPF,
        'salonG': salonG,
        'salonP': salonP,
        'salonS': salonS,
        }
    return render(request, 'salon.html', context)
