from django.urls import path
from .import views

urlpatterns = [
    path("",views.dashBoard,name="dashBoard"),
    path("addCompany/",views.addBrand,name="addBrand"),
    path("addMobile/",views.addMobiles,name="addMobiles"),
    path("deleteMobile/<str:mobile_id>/",views.deleteMobile,name="deleteMobile"),
    path("editMobile/<str:mobile_id>/",views.editMobile,name="editMobile"),
]
