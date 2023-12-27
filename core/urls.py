"""core URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.production.urls')),
    path('users/', include('apps.users.urls')),
]
