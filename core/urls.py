"""core URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('production/', include('apps.production.urls')),
    path('', include('apps.users.urls')),
]
