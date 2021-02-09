from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name="Home"),
    path('register/', views.register, name="Register"),
    path('login/', views.login, name="Login"),
    path('login/admin/', admin.site.urls),
    path('logout', views.logout, name="logout"),
]
