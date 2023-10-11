from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.mylogin, name='login'),
    path('signup/', views.register, name='signup'),
    path('logout/', views.mylogout, name='logout'),

]
