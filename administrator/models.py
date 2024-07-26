from django.db import models

<<<<<<< HEAD

class GaleryWorck(models.Model):
    imagen = models.ImageField(upload_to='galeryWorckIMG/', null=False, blank=False)
    
class GaleryClient(models.Model):
    imagen = models.ImageField(upload_to='galeryClientIMG/', null=False, blank=False)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=50)


class Receta(models.Model):
    recipe = models.CharField(max_length=75, null=False, blank=False, verbose_name="Nombre")
    price = models.IntegerField(null=False, blank=False)
    price_alter = models.IntegerField(null=False, blank=False)
    descrip = models.CharField(max_length=195, null=False, blank=False)
    time_out = models.IntegerField(null=False, blank=False)
    imagen = models.ImageField(upload_to='recipeIMG/', null=False, blank=False)
    steps = models.CharField(max_length=1500, null=False, blank=False)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', related_name='recetas')
    category = models.CharField(max_length=50, null=False, blank=False)
    place = models.CharField(max_length=11, null=False, blank=False)
    active = models.CharField(max_length=2, null=False, blank=False, default="Sí")
    galery_worck = models.ManyToManyField(GaleryWorck, through='RecipeGaleryW', related_name='galeryW')
    galery_client = models.ManyToManyField(GaleryClient, through='RecipeGaleryC', related_name='galeryC')
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_recipes')

class RecipeGaleryW(models.Model): 
    recipe = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='recipe_galeryW')
    image = models.ForeignKey(GaleryWorck, on_delete=models.CASCADE, related_name='image_recipes')
    
class RecipeGaleryC(models.Model): 
    recipe = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='recipe_galeryC')
    image = models.ForeignKey(GaleryClient, on_delete=models.CASCADE, related_name='imageC_recipes')
=======
# Create your models here.
>>>>>>> 800db762a542d7ba1511d3ceaf6b32a37e3cc2ec
