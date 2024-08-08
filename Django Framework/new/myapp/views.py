from django.shortcuts import render
from django.http import HttpResponse

from .models import Fruit
# Create your views here.

def read(request):
    fruits = Fruit.objects.all()
    context = {
        'fruits' : fruits
    }
    return render(request,'myapp/read.html',context)