from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/',views.homeView,name="homeView"),
    # path('',views.loginView,name="loginView"),
    # path('registration/',views.registerView,name="registerView"),
]
