from django.urls import path
from . import views


urlpatterns = [
    # pk is a dynamic string value
    path('projects/<str:pk>/', views.projects, name="projects"),
    path('project-archive/', views.project_archive, name="project-archive"),
]