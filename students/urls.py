from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('dashboard/', views.student_dashboard, name='dashboard'),
    path('application/', views.application, name='application'),

    path("get-subcounties/<str:county_name>/", views.get_subcounties, name="get_subcounties"),  # Change from int to str
    path("family/", views.family_background_view, name="family"),
]
