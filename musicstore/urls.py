from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.home_view, name="home"),
    path('index',views.index_view,name="index"),
    path('home',views.home_view, name="home"),
    path('register',views.register_request, name="register"),
    path('login', views.login_request, name="login"),
    path('admin/',admin.site.urls),
    path('logout/',LogoutView.as_view(next_page = 'home'),name='logout'),
]