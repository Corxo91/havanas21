# Generated by Django 5.0.3 on 2024-07-18 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0008_galeryworck_recipegaleryw_receta_galery_worck'),
    ]

    operations = [
        migrations.CreateModel(
            name='GaleryClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='galeryClientIMG/')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeGaleryC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imageC_recipes', to='administrator.galeryclient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_galeryC', to='administrator.receta')),
            ],
        ),
        migrations.AddField(
            model_name='receta',
            name='galery_client',
            field=models.ManyToManyField(related_name='galeryC', through='administrator.RecipeGaleryC', to='administrator.galeryclient'),
        ),
    ]
