from django.shortcuts import render
from django.http import HttpResponse
from blogs import models
from django.contrib import messages
def index(request):
    return render(request, 'index.html')
def intro(request):
    return render(request, 'intro.html')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        isClient = 1 if (request.POST['isClient']).lower() == 'on' else 0
        user = models.contactTable()
        user.nameC = name
        user.emailC = email
        user.phoneC = phone
        user.isClient = isClient
        user.save()
        params = {
            'message' : messages.success,
        }
        return render(request, 'contact.html', params)
    return render(request, 'contact.html')
def service(request):
    return render(request, 'service.html')