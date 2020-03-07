from django.urls import path
from . import views

urlpatterns = [
    path('HomePage',views.HomePage,name= 'Homepage'),
    path('InputForm',views.InputForm,name= 'InputForm'),
    path('Output',views.Output,name= 'Output'),
    path('Aptitude', views.aptitude, name = 'Aptitude')
] 
