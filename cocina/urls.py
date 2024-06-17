from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.cocina, name='cocina'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)