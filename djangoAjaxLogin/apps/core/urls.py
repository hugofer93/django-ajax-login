from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('home', views.Home.as_view(), name='home'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
]