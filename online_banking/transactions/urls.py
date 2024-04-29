from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('view_balance', views.view_balance, name = 'view_balance'),
    path('withdraw', views.withdraw, name = 'withdraw'),
    path('deposit', views.deposit, name = 'deposit'),
    path('transfer', views.transfer, name = 'transfer'),
]
