from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('increment/', views.increment, name='increment'),
    path('decrement/', views.decrement, name='decrement'),
    path('reset/', views.reset, name='reset'),
]