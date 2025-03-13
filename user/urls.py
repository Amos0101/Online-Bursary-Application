from django.urls import path
from .views import register, student_login, student_logout, home, admin_register, admin_login, admin_home

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', student_login, name='login'),
    path('logout/', student_logout, name='logout'),
    path('home/', home, name='home'),

    path("admin-register/", admin_register, name="admin_register"),
    path("admin-login/", admin_login, name="admin_login"),
    path("admin-home/", admin_home, name="admin_home"),
]
