from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('new/', views.new_post, name='new_post'),
]

