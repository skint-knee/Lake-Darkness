from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def project_archive(request):
    return HttpResponse('project archive')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('analyst_form.urls'))

]

