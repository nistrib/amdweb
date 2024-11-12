from django.urls import path
from . import views


# If want to use without log in page at start
# urlpatterns = [
#     path('login/', views.login_view, name='login'),
#     path('', views.home, name='home'),
#     path('project_control_center/', views.project_control_center, name='project_control_center'),
#
#     path('about/', views.about, name='about'),
# ]



# If want to use with a log in page
urlpatterns = [
    path('', views.login_view, name='login'),  # Set the login view as the default route
    path('home/', views.home, name='home'),  # Make home accessible after login
    path('project_control_center/', views.project_control_center, name='project_control_center'),
    path('about/', views.about, name='about'),


# Here is the part for button
    path('project_control_center/turn_on/', views.update_status, name='turn_on'),  # Route for ON action
    path('project_control_center/turn_off/', views.update_status, name='turn_off'),  # Route for OFF action
    path('project_control_center/get_status/', views.get_status, name='get_status'),  # Endpoint for Arduino


]