# Generated by Django 5.0.3 on 2024-07-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0009_galeryclient_recipegaleryc_receta_galery_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='descrip',
            field=models.CharField(max_length=1500),
        ),
    ]
