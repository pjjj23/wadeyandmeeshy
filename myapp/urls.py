from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page 
    path('gallery/', views.gallery, name='gallery'),
    path('lily/', views.lily, name='lily'),
]
