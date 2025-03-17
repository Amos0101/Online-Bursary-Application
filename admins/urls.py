
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin_homepage/', views.admin_homepage, name='admin_homepage'),
    path('applications/', views.review_applications, name='review_applications'),

    path('application/<int:app_id>/', views.review_application_details, name='review_application_details'),

    path('approved-applications/', views.approved_applications, name='approved_applications'),
    path('rejected-applications/', views.rejected_applications, name='rejected_applications'),

]
