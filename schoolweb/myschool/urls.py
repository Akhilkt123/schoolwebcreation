from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
     path('register/', views.regform, name='regform'),
    # path('regsuccess/', views.reg_success, name='regsuccess'),

]
