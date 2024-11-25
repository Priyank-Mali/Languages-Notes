from django.urls import path
from  .import views

urlpatterns = [
    path('categories/',views.productCategoryList,name='productCategoryList'),
    path('products/',views.productList,name='productList')
]
