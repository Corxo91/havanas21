from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.welcome_view, name='bienvenida'),
    path('login/', views.login_view, name='login'),
    path('tools/', include('cocina.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)