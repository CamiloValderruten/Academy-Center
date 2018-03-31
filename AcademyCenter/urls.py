from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('home.urls', namespace="home")),
    path('dashboard/', include('dashboard.urls'), name='dashboard'),
    path('api/', include('core.urls'), name='api'),
    path('admin/', admin.site.urls, name='admin'),
]
