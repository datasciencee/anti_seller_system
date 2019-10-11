from django.urls import path, include
from . import views


urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),


    path('merchant/', views.merchant),
    path('monitor/', views.monitor),

    path('user_information/', views.user_information),
    path('add_user_information/', views.add_user_information)
]

