# Generated by Django 5.0.3 on 2024-06-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0005_alter_receta_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='price_alter',
            field=models.FloatField(),
        ),
    ]