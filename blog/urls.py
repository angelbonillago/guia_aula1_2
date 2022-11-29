from django.urls import path
from . import views
  
urlpatterns = [
    path('nueva/', views.index),

]
  
  
