from django.urls import path
from . import views
from . import Productdetails
from . import Productdetails
urlpatterns = [
    path('hamid/', views.Home.as_view(), name='home'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('productsdetail/<int:product_id>/', Productdetails.productDetails.as_view(), name='product_detail'),
    path('productscreate/', views.ProductCreate.as_view(), name='product_create'),
    path('productsupdate/<int:product_id>', views.ProductUpdate.as_view(), name='product_update'),
    path('productdelete<int:product_id>', views.ProductDelete.as_view(), name='product_delete'),
]