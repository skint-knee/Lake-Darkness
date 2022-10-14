from django.urls import path

from . import views

urlpatterns = [
    # pk is a dynamic string value
    path('', views.project_form, name="project-form"),
    path('projects/<str:pk>/', views.projects, name="projects"),
    
]