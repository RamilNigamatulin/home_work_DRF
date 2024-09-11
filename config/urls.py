from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('materials/', include('materials.urls', namespace='materials')),
    path('users/', include('users.urls', namespace='users')),
]
