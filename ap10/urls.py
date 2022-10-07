from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('second/', views.second, name='second'),
    path('second/addrecord/', views.addrecord, name='addrecord'),
    
]
