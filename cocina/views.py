from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
<<<<<<< HEAD
from administrator.models import Receta

@login_required
def cocina(request):
    recipeEP = Receta.objects.filter(place="Restaurante", category="Entre Panes").order_by('recipe')
    recipeEF = Receta.objects.filter(place="Restaurante", category="Entrantes Fríos").order_by('recipe')
    recipeEC = Receta.objects.filter(place="Restaurante", category="Entrantes Calientes").order_by('recipe')
    recipeCI = Receta.objects.filter(place="Restaurante", category="Cocina Italiana").order_by('recipe')
    recipePF = Receta.objects.filter(place="Restaurante", category="Platos Fuertes").order_by('recipe')
    recipeG = Receta.objects.filter(place="Restaurante", category="Guarniciones").order_by('recipe')
    recipeP = Receta.objects.filter(place="Restaurante", category="Postres").order_by('recipe')
    recipeCa = Receta.objects.filter(place="Bar", category="Cafés").order_by('recipe')
    recipeCo = Receta.objects.filter(place="Bar", category="Bebidas").order_by('recipe')
    context = {
        'recipeEP' : recipeEP,
        'recipeEF' : recipeEF,
        'recipeEC' : recipeEC,
        'recipeCI' : recipeCI,
        'recipePF' : recipePF,
        'recipeG' : recipeG,
        'recipeP' : recipeP,
        'recipeCa' : recipeCa,
        'recipeCo' : recipeCo,
    }
    return render(request, 'tools.html', context)

def info(request):
    if request.method == 'POST':
        recipeID = request.POST.get('id')
        recipe = Receta.objects.get(id=recipeID)
        ingredientes = recipe.ingredients.all()
        galery = recipe.galery_worck.all()
    context = {
        'recipe': recipe,
        'ingredientes': ingredientes,
        'galery': galery
    }    
    return render(request, 'info_cocina.html', context)
=======

@login_required
def cocina(request):
    return render(request, 'tools.html', {})
>>>>>>> 800db762a542d7ba1511d3ceaf6b32a37e3cc2ec

def logout_view(request):
    logout(request)
    return redirect('bienvenida')