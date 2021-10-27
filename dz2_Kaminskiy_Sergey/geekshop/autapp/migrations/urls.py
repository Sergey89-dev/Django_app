from django.urls import path
from autapp import views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login,name= 'login'),
    path('logout/', authapp.login,name= 'logout')
]
