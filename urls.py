from django.urls import path
from . import views
urlpatterns=[
    path('', views.login, name='slot booking'),
    path('login',views.login,name='slot booking'),
    path('home',views.home,name='slot booking'),
    path('booking', views.booking, name='slot booking'),
    path('confirm', views.confirm, name='slot booking'),
]