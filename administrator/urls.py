from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.admin, name='admin'),
    path('add_recipe/', views.create_recipe, name='add'),
    path('changeStatus/', views.status, name='status'),
    path('edit/', views.edit, name='edit'),
    path('changeEdit/', views.changeEdit, name='changeEdit'),
    path('photoEdit/', views.editGW, name='editGW'),
    path('photoEditC/', views.editGC, name='editGC'),
    path('createUser/', views.createUser, name='createUser'),
    path('deleteUser/', views.deleteUser, name='deleteUser'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('addIngre/', views.addIngre, name='addIngre'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)