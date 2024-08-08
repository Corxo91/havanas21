import os
import django
from getpass import getpass
import sys

# Establece la configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "havanas21.settings")
django.setup()

from login.models import User

def get_secure_password():
    password = b""
    while True:
        try:
            password = getpass("Ingresa la contraseña: ", stream=sys.stderr).encode()
            confirm_password = getpass("Confirma la contraseña: ", stream=sys.stderr).encode()
            if password == confirm_password:
                return password.decode()
            else:
                print("Las contraseñas no coinciden. Intenta de nuevo.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperación cancelada.")
            sys.exit(1)

def create_user(username, password):
    while True:
        # Verifica si es usuario de cocina
        is_cocina = input("¿Es usuario de cocina? (si/no): ")
        if is_cocina.lower() == "si":
            user = User.objects.create_user(
                username=username,
                password=password,
                if_cocina=True,
                if_bar=False,
                is_superuser=False,
                if_admin=False,
                if_comercial=False,
                if_economica=False,
            )
            print(f"Usuario de cocina '{user.username}' creado exitosamente.")
            return

        # Verifica si es usuario de bar
        is_bar = input("¿Es usuario de bar? (si/no): ")
        if is_bar.lower() == "si":
            user = User.objects.create_user(
                username=username,
                password=password,
                if_cocina=False,
                if_bar=True,
                is_superuser=False,
                if_admin=False,
                if_comercial=False,
                if_economica=False,
            )
            print(f"Usuario de bar '{user.username}' creado exitosamente.")
            return

        # Verifica si es usuario administrador
        is_admin = input("¿Es usuario administrador? (si/no): ")
        if is_admin.lower() == "si":
            if_comercial = input("¿Es comercial? (si/no): ")
            if if_comercial.lower() == "si":
                user = User.objects.create_user(
                username=username,
                password=password,
                if_cocina=False,
                if_bar=False,
                is_superuser=False,
                if_admin=False,
                if_comercial=True,
                if_economica=False,
                )
                print(f"Usuario comercial '{user.username}' creado exitosamente.")
            
            else:
                if_economica = input("¿Es económica/o? (si/no): ")
                if if_economica.lower() == "si":
                    user = User.objects.create_user(
                    username=username,
                    password=password,
                    if_cocina=False,
                    if_bar=False,
                    is_superuser=False,
                    if_admin=False,
                    if_comercial=False,
                    if_economica=True,
                    )
                    print(f"Usuario económica/o '{user.username}' creado exitosamente.")
                else :
                    user = User.objects.create_user(
                    username=username,
                    password=password,
                    if_cocina=False,
                    if_bar=False,
                    is_superuser=True,
                    if_admin=True,
                    if_comercial=False,
                    if_economica=False,
                    )
                    print(f"Usuario administradorcomer '{user.username}' creado exitosamente.")
            return

        print("No se ha seleccionado ningún tipo de usuario válido. Intenta de nuevo.")

# Solicita los datos del usuario
username = input("Ingresa el nombre de usuario: ")
password = get_secure_password()

create_user(username, password)