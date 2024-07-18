from django.urls import path
from .import views

urlpatterns = [
    path('',views.booklistview,name='booklistview'),
    path('add-book/',views.addbookview,name='addbookview'),
    path('edit-book/<int:pk>/',views.updatebook,name='updatebook'),
    path('delete-book/<int:pk>/',views.deletebook,name='deletebook'),
]
