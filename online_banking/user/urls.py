from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_index, name = 'user_index'),
    path('create_user', views.create_user, name = 'create_user'),

]
