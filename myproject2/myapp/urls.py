from django.urls import path
from . import views
from myapp.views import  product_list, delete_product

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('upload/', views.upload_product, name='upload_product'),
    path('product/<int:product_id>/delete/', delete_product, name='delete_product'),   
]
