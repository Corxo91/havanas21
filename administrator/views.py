from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import default_storage
from .models import Receta, Ingredient, GaleryWorck, RecipeGaleryW, GaleryClient, RecipeGaleryC
from login.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os


@login_required
def admin(request):
    receta = Receta.objects.filter(place="Restaurante")
    trago = Receta.objects.filter(place="Bar")
    actived = Receta.objects.filter(active="Sí", place="Restaurante")
    activedB = Receta.objects.filter(active="Sí", place="Bar")
    users = User.objects.all().order_by('username')
    context = {
        'receta': receta,
        'trago': trago,
        'actived': actived,
        'activedB': activedB,
        'users': users,
    }
    return render(request, 'administrador.html', context)

def create_recipe(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST.get('name')
        price = request.POST.get('price')
        alter_price = request.POST.get('alter')
        steps = request.POST.get('steps')
        descript = request.POST.get('descript')
        cooking_time = request.POST.get('time')
        imagen = request.FILES.get('imagen')
        category = request.POST.get('category')
        place = request.POST.get('lugar')
        images = request.FILES.getlist('images[]')
        imagesC = request.FILES.getlist('imagesC[]')
        
        # Crear la nueva receta
        recipe = Receta.objects.create(
            recipe=name,
            price=price,
            price_alter=alter_price,
            steps=steps,
            descrip=descript,
            time_out=cooking_time,
            imagen=imagen,
            category=category,
            place=place
        )
        

        #Crear las imágenes de trabajadores        
        for image in images:
            galery = GaleryWorck(imagen=image)
            galery.save()
            recipe.galery_worck.add(galery)
            
        for imageC in imagesC:
            galeryC = GaleryClient(imagen=imageC)
            galeryC.save()
            recipe.galery_client.add(galeryC)
    
        # Crear o actualizar los ingredientes
        for i in range(1, 20):
            ingredient_name = request.POST.get(f'ing{i}')
            ingredient_amount = request.POST.get(f'cant{i}')
            if ingredient_name and ingredient_amount:
                ingredient = Ingredient.objects.create(
                    name=ingredient_name,
                    amount=ingredient_amount
                )
            recipe.ingredients.add(ingredient)
        messages.success(request,f'{category} {name} creada exitosamente')    
        return redirect('admin')
    else:
        return render(request, "administrador.html")

def status(request): 
    if request.method == 'POST':
        id_receta = request.POST.get('id_receta')
                # Buscar la receta por el id
        try:
            receta = Receta.objects.get(id=id_receta)
        except Receta.DoesNotExist:
            # Si no se encuentra, redirigir de vuelta
            return redirect('admin')
        
        # Cambiar el estado del atributo 'active'
        if receta.active == "Sí":
            receta.active = "No"
        else:
            receta.active = "Sí"
        
        # Guardar los cambios
        receta.save()
    return redirect('admin')

def edit(request):
    if request.method == 'POST':
        id_receta = request.POST.get('id_receta')
        recipe = Receta.objects.get(id=id_receta)
        ingrediens = recipe.ingredients.all()
        imagesW = recipe.galery_worck.all()
        imagesC = recipe.galery_client.all()
        contador = 0
        cont = 0
        conta = 0
        for i in ingrediens:
            contador+=1    
        for e in imagesW: 
            cont+=1
        for j in imagesC:
            conta+=1
    context = {
        'recipe': recipe,
        'ingrediens': ingrediens,
        'contador': contador,
        'imagesW': imagesW,
        'imagesC': imagesC,
        'cont': cont,
        'conta': conta 
    }
    if request.user.if_admin:
        return render(request, 'edit_recipe.html', context)
    elif request.user.if_comercial:
        return render(request, 'edit_comercial.html', context)
    elif request.user.if_economica:
        return render(request, 'edit_eco.html', context)

def changeEdit(request):
    if request.method == 'POST':
        id_receta = request.POST.get('id_recipe')
        recipe = request.POST.get('recipe')
        descrip = request.POST.get('descrip')
        steps = request.POST.get('steps')
        price = request.POST.get('price')
        price_alter = request.POST.get('price_alter')
        time_out = request.POST.get('time_out')
        counter = request.POST.get('counter')
        imagen = request.FILES.get('imagen')
        cont = int(counter)+1
        
        for i in range(1, cont):
            ingredient_name = request.POST.get(f'ingredient{i}')
            ingredient_amount = request.POST.get(f'amount{i}')
            id_ingre = request.POST.get(f'id_ingre{i}')
            Ingredient.objects.filter(id=id_ingre).update(name=ingredient_name, amount=ingredient_amount)
            
        if  'imagen' in request.FILES:
            receta = Receta.objects.get(id=id_receta)
            if receta.imagen and imagen:
            # Si la imagen cambia, elimina la antigua
                if os.path.isfile(receta.imagen.path):
                    os.remove(receta.imagen.path)
            receta.imagen = imagen
            receta.save()
                    
        Receta.objects.filter(id=id_receta).update(recipe=recipe, descrip=descrip, steps=steps, price=price, price_alter=price_alter, time_out=time_out)
            
    return redirect('admin')

def addIngre(request):
    if request.method == 'POST':
        id_recipe = request.POST.get('id_recipe')
        name = request.POST.get('ingrediente')
        amount = request.POST.get('cantidad')
        
        recipe = Receta.objects.get(id=id_recipe)
        
        new_ingredient = Ingredient(name=name, amount=amount)
        new_ingredient.save()
        
        recipe.ingredients.add(new_ingredient)
        
        messages.success(request, 'Se actualizó correctamente el ingrediente.' )
    return redirect('admin')

def editGW(request):
    if request.method == 'POST':
        id_receta = request.POST.get('id_recipe')
        recipe = Receta.objects.get(id=id_receta)


    #Procesar el borrado
        cuenta = request.POST.get('cuenta')    
        cuent = int(cuenta)+1
        for e in range(1, cuent):
            id_img = request.POST.get(f'imagenID{e}')
            if id_img != 'null':
                image = GaleryWorck.objects.get(id=id_img)               
                # Construir la ruta del archivo en la carpeta media
                file_name = f"{image.imagen}"  # Asumiendo que el nombre del archivo es igual al ID
                file_path = f"{settings.MEDIA_ROOT}/{file_name}"
                # Eliminar el archivo de imagen del sistema
                try:
                    if default_storage.exists(file_path):
                        default_storage.delete(file_path)
                except Exception as e:
                    print(f"Error al eliminar el archivo {file_path}: {str(e)}")
                
                RecipeGaleryW.objects.filter(image_id=id_img).delete()
                GaleryWorck.objects.filter(id=id_img).delete()
    
    #Procesar agrego de imágenes
        images = request.FILES.getlist('photos[]')
        for image in images:
            galery = GaleryWorck(imagen=image)
            galery.save()
            recipe.galery_worck.add(galery)
            
    return redirect('admin')

def editGC(request):
    if request.method == 'POST':
        id_receta = request.POST.get('id_recipeC')
        recipe = Receta.objects.get(id=id_receta)

    #Procesar el borrado
        cuenta = request.POST.get('cuentaC')    
        cuent = int(cuenta)+1
        for e in range(1, cuent):
            id_img = request.POST.get(f'imagenIDC{e}')
            if id_img != 'null':
                image = GaleryClient.objects.get(id=id_img)               
                # Construir la ruta del archivo en la carpeta media
                file_name = f"{image.imagen}"  # Asumiendo que el nombre del archivo es igual al ID
                file_path = f"{settings.MEDIA_ROOT}/{file_name}"
                # Eliminar el archivo de imagen del sistema
                try:
                    if default_storage.exists(file_path):
                        default_storage.delete(file_path)
                except Exception as e:
                    print(f"Error al eliminar el archivo {file_path}: {str(e)}")
                
                RecipeGaleryC.objects.filter(image_id=id_img).delete()
                GaleryClient.objects.filter(id=id_img).delete()
    
    #Procesar agrego de imágenes
        images = request.FILES.getlist('photosC[]')
        for image in images:
            galery = GaleryClient(imagen=image)
            galery.save()
            recipe.galery_client.add(galery)
            
    return redirect('admin')

def createUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('repass').encode()
        rol = request.POST.get('rol')
        if rol == 'if_cocina':
            user = User.objects.create_user(
                username=username,
                if_cocina=True,
                if_bar=False,
                is_superuser=False,
                if_admin=False,
                if_comercial=False,
                if_economica=False,
            )
            user.set_password(password)
            user.save()
            messages.success(request,f'Usuario {username} cocina creado exitosamente.')
        elif rol == 'if_bar':
            user = User.objects.create_user(
                username=username,
                if_cocina=False,
                if_bar=True,
                is_superuser=False,
                if_admin=False,
                if_comercial=False,
                if_economica=False,
            )
            user.set_password(password)
            user.save()
            messages.success(request,f'Usuario {username} bar creado exitosamente.')
        elif rol == 'if_comercial':
            user = User.objects.create_user(
                username=username,
                if_cocina=False,
                if_bar=False,
                is_superuser=False,
                if_admin=False,
                if_comercial=True,
                if_economica=False,
                )
            user.set_password(password)
            user.save()
            messages.success(request,f'Usuario {username} comercial creado exitosamente.')
        elif rol == 'if_economica':
            user = User.objects.create_user(
                    username=username,
                    if_cocina=False,
                    if_bar=False,
                    is_superuser=False,
                    if_admin=False,
                    if_comercial=False,
                    if_economica=True,
                    )
            user.set_password(password)
            user.save()
            messages.success(request,f'Usuario {username} económica creado exitosamente.')
        else:
            user = User.objects.create_user(
                    username=username,
                    if_cocina=False,
                    if_bar=False,
                    is_superuser=True,
                    if_admin=True,
                    if_comercial=False,
                    if_economica=False,
                    )
            user.set_password(password)
            user.save()
            messages.success(request,f'Usuario {username} administrador creado exitosamente.')

    return redirect('admin')

def deleteUser(request):
    if request.method == 'POST':
        user = request.POST.get('deleteUser')
        usuario = User.objects.get(username=user)
        if usuario.if_admin:
            otros_admins = User.objects.filter(if_admin=True).exclude(id=usuario.id)
            if otros_admins.exists():
                User.objects.get(username=user).delete()
                messages.success(request,f'Usuario eliminado exitosamente')
            else:
                messages.error(request,f'No hay más administradores, no se puede borrar su usuario')
        else:    
            User.objects.get(username=user).delete()
            messages.success(request,f'Usuario eliminado exitosamente')
        
    return redirect('admin')

def changePassword(request):
    if request.method == 'POST':
        ussr = request.POST.get('passwordReset')
        new_password = request.POST.get('repasword').encode()
        
        user = User.objects.get(username=ussr)
        user.set_password(new_password)
        user.save()
        messages.success(request,f'Se ha actualizado correctamente la clave.')
    return redirect('admin')