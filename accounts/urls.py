from django.urls import path
from . import views
urlpatterns = [
    path('logout/', views.log_out),
    path('login/', views.log_in),
    path('register/', views.register),
    path('', views.account_index),
]
