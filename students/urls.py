from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('dashboard/', views.student_dashboard, name='dashboard'),

    path("student_application/", views.student_application, name="student_application"),

    path("confirm_application/", views.confirm_application, name="confirm_application"),
    path("success/", lambda request: render(request, "application_success.html"), name="application_success"),
]
