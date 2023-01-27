from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_payment_order, name='create_payment_order'), 
    path('', views.view_payment_order, name='view_payment_order')
]