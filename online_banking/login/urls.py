from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout')

]
