from django.db import models
from django.utils.text import Truncator


class GaleryWorck(models.Model):
    imagen = models.ImageField(upload_to='galeryWorckIMG/', null=False, blank=False)
    
class GaleryClient(models.Model):
    imagen = models.ImageField(upload_to='galeryClientIMG/', null=False, blank=False)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=50)


class Receta(models.Model):
    recipe = models.CharField(max_length=75, null=False, blank=False, verbose_name="Nombre")
    price = models.FloatField(null=False, blank=False)
    price_alter = models.FloatField(null=False, blank=False)
    descrip = models.CharField(max_length=200, null=False, blank=False)
    descrip_en = models.CharField(max_length=200, null=False, blank=False, default='Agregar la traducción aki de la descripción')
    time_out = models.CharField(max_length=7,null=False, blank=False)
    imagen = models.ImageField(upload_to='recipeIMG/', default='noPhoto.jpg', blank=True, null=True)
    steps = models.CharField(max_length=1500, null=False, blank=False)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', related_name='recetas')
    category = models.CharField(max_length=50, null=False, blank=False)
    place = models.CharField(max_length=11, null=False, blank=False)
    active = models.CharField(max_length=2, null=False, blank=False, default="Sí")
    galery_worck = models.ManyToManyField(GaleryWorck, through='RecipeGaleryW', related_name='galeryW')
    galery_client = models.ManyToManyField(GaleryClient, through='RecipeGaleryC', related_name='galeryC')
    
    def save(self, *args, **kwargs):
        if not self.id:  # Solo para nuevos objetos
            if not self.imagen:  # Si no hay imagen desde el formulario
                self.imagen = 'noPhoto.png'  # Usa el valor predeterminado
            super().save(*args, **kwargs)
        else:
            # Para objetos existentes, mantén el valor actual si ya existe
            super().save(*args, **kwargs)

    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_recipes')

class RecipeGaleryW(models.Model): 
    recipe = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='recipe_galeryW')
    image = models.ForeignKey(GaleryWorck, on_delete=models.CASCADE, related_name='image_recipes')
    
class RecipeGaleryC(models.Model): 
    recipe = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='recipe_galeryC')
    image = models.ForeignKey(GaleryClient, on_delete=models.CASCADE, related_name='imageC_recipes')
