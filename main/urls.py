from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),

    path('', views.home, name='home'),

    path('project_control_center/', views.project_control_center, name='project_control_center'),

    path('about/', views.about, name='about'),
]

# path('projects/<int:pk>/', views.project_detail, name='project_detail'),