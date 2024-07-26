#from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('client/', include('cliente.urls')),
<<<<<<< HEAD
    path('administrador/', include('administrator.urls')),
=======
    path('administrador/', include('administrator.urls'))
>>>>>>> 800db762a542d7ba1511d3ceaf6b32a37e3cc2ec
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)