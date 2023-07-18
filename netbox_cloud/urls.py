from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('containers/', views.ContainersView.as_view(), name='containers'),
]