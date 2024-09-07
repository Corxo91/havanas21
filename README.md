Para realizar el despliegue del proyecto necesita minimo python 3.12.0
Es necesario tener instalado virtualenv


Pasos para desplegar completamente el proyecto.
Crear un entorno virtual dentro de el directorio raiz del proyecto.
  python -m venv venv
Activar el venv 
  cd  source venv/Scripts/activate
Instalar el requirements.txt
  pip install -p requirements.txt
Correr en local: python manage.py runserver

Correr publico:
  Modificar el archivo runserver.py
  Sustituir el ip y el puerto por el ip de su computador y el puerto que desee usar.
  Ejecutar python runserver.py
