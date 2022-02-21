from django.urls import path
from . import views

urlpatterns = [
  path('', views.super_type),
  path('<int:pk>/', views.super_type_detail)
]
