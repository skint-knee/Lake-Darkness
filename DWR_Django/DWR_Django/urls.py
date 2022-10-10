from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
# we defined the projects function to require a parameter "pk" or primary key
# these functions are technically views and shouldn't be here
def projects(request, pk):
    return HttpResponse('Here is the basic response {}'.format(pk))
 
def project_archive(request):
    return HttpResponse('project archive')
 
urlpatterns = [
    path('admin/', admin.site.urls),
    # pk is a dynamic string value
    path('projects/<str:pk>/', projects, name="projects"),
    path('project-archive/', project_archive, name="project-archive"),
]

