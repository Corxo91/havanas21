from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('cocina/', include('cocina.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)