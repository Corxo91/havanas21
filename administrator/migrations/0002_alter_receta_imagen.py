# Generated by Django 5.0.3 on 2024-06-24 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(upload_to='recipeIMG/'),
        ),
    ]
