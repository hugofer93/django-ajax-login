from django.urls import path

from project.apps.core.views import Home, Index, Login, Logout

app_name = 'core'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('home/', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
