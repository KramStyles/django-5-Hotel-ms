from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='acc-home'),
    path('login', views.login, name='acc-login'),
    path('register', views.register, name='acc-register'),
]
