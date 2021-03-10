from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('quote', views.quote, name='register'),
    path('history', views.history, name='history'),
    path('profile', views.profile, name='profile')
]