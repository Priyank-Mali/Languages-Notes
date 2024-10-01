from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Mobile,Brand
from django.contrib import messages

# Create your views here.

def dashBoard(request):
    if request.method == "GET":
        search_ = request.GET.get("search")
        if search_:
            mobile_queryset = Mobile.objects.filter(brand_name__name__icontains = search_) | Mobile.objects.filter(model_name__icontains = search_) | Mobile.objects.filter(price__icontains = search_)

        else:
            mobile_queryset = Mobile.objects.all()

    context = {
        "mobiledata" : mobile_queryset,
    }
    return render(request,"myapp/dashboard.html",context)


def addBrand(request):

    if request.method == "POST":
        companyName_ = request.POST.get("companyName").capitalize()
        if Brand.objects.filter(name=companyName_).exists():
            return render(request,"myapp/addCompany.html",{"msg" : f"{companyName_} is already exists"})
            
        else:    
            Brand.objects.create(
                name = companyName_
            )
            return render(request,"myapp/addCompany.html",{"msg" : f"{companyName_} added successfully"})
        
    return render(request,"myapp/addCompany.html")

def addMobiles(request):
    brands_objects = Brand.objects.all()

    if request.method == "POST":
        brand_name_ = request.POST.get("brand_name").capitalize()
        model_name_ = request.POST.get("model_name").capitalize()
        price_ = request.POST.get("price")
        image_ = request.FILES.get("image")

        if brand_name_ == "":
            return render(request,"myapp/addMobile.html", {"msg" : "Please Select Brand"})
        
        brand_object = Brand.objects.get(name=brand_name_)

        if Mobile.objects.filter(model_name = model_name_).exists():
            return render(request,"myapp/addMobile.html", {"msg" : f"{model_name_} is already exists in database"})
        
        try:
            price_ = float(price_)
        except ValueError:
            return render(request,"myapp/addMobile.html", {"msg" : "Invalid Price"})

        new_object = Mobile(
            brand_name = brand_object,
            model_name = model_name_,
            price = price_,
            image = image_
        )
        new_object.save()
        return render(request,"myapp/addMobile.html", {"msg" : f"{brand_name_} {model_name_} is added successfully in database"})

    return render(request,"myapp/addMobile.html",{"brands" : brands_objects})


def deleteMobile(request,mobile_id):
    mobile_object = Mobile.objects.get(mobile_id=mobile_id)
    if request.method == "POST":
        mobile_object.delete()
        return redirect("dashBoard")

    return render(request,"myapp/deleteConfirm.html",{"obj" : mobile_object})

def editMobile(request,mobile_id):
    mobile_object = Mobile.objects.get(mobile_id=mobile_id)

    if request.method == "POST":
        model_name_ = request.POST.get("model_name")
        price_ = request.POST.get("price")
        image_ = request.FILES.get("image")
        description_ = request.POST.get("description")

        try:
            price_ = float(price_)
        except ValueError:
            return render(request,"myapp/editMobile.html",{"error" : "Invalid Price"})

        if model_name_:
            mobile_object.model_name = model_name_
        if price_:
            mobile_object.price = price_
        if image_:
            mobile_object.image = image_
        if description_:
            mobile_object.description = description_
        mobile_object.save()
        return render(request,"myapp/editMobile.html",{"success" : "Data Updated Successfully"})


    return render(request,"myapp/editMobile.html",{"obj" : mobile_object})