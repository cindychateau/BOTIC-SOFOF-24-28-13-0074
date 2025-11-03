from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]