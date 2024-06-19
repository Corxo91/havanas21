from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('cafe/', views.bar, name='bar'),
    path('restaurante/', views.salon, name='salon'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)