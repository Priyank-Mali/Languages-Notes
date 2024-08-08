from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

def homeView(request):
    getuser = User.objects.all()
    context = {
        "users" : getuser
    }
    return render(request,"myapp/dashboard.html",context)
    