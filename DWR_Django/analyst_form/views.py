from django.shortcuts import render
from django.http import HttpResponse
# we defined the projects function to require a parameter "pk" or primary key
# these functions are technically views and shouldn't be here
def projects(request, pk):
    return HttpResponse('Here is the basic response {}'.format(pk))
 
def project_form(request):
    return render(request, 'analyst_form.html')