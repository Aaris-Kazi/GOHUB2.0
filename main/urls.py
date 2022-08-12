from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name="log"),
    path('register/', views.register),
    path('search/', views.search, name='search'),
    path('search2/', views.search2, name='search2'),
    path('logout/', views.user_logout, name='logout'),
]
