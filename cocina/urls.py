from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.cocina, name='cocina'),
    path('logout/', views.logout_view, name='logout'),
<<<<<<< HEAD
    path('informacion/', views.info, name='info'),
=======
>>>>>>> 800db762a542d7ba1511d3ceaf6b32a37e3cc2ec
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)