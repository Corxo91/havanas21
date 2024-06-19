# Generated by Django 5.0.3 on 2024-06-18 00:54

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0014_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'Este nombre de usuario ya existe.'}, help_text='Máximo 15 caracteres y mínimo 4.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Usuario')),
                ('first_name', models.CharField(help_text='Tiene que empezar con letra mayúscula.', max_length=150, verbose_name='Nombre')),
                ('last_name', models.CharField(help_text='Solo use espacio en apellidos compuestos.', max_length=150, verbose_name='Apellido')),
                ('email', models.EmailField(help_text='Solo se permiten correos UCI', max_length=254, verbose_name='Correo')),
                ('is_staff', models.BooleanField(default=False, help_text='Has sido designado por el administrado como Staff', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Usuario creadoUsuario eliminado', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('if_cocina', models.BooleanField()),
                ('if_bar', models.BooleanField()),
                ('if_admin', models.BooleanField()),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
