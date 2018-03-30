from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('features', views.features, name='features'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.pricing, name='pricing'),
    path('register', views.register, name='register'),
]
