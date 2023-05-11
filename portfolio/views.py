from django.shortcuts import render
from django.http import HttpResponse
from blogs import models

def index(request):
    return render(request, 'index.html')
def intro(request):
    return render(request, 'intro.html')
def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('emailHelp')
    phone = request.POST.get('phone')
    text = request.POST.get('name')
    user = models.contactTable
    user.nameC = name
    user.emailC = email
    user.phoneC = phone
    
    return render(request, 'contact.html')
def service(request):
    return render(request, 'service.html')