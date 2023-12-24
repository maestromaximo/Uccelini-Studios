# mainapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customize/', views.customize, name='customize'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact_us, name='contact')
]
