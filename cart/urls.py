# cart/urls.py
from django.urls import path
from .views import (
    home, 
    cart_page, 
    product_detail_view, 
    add_to_cart_api, 
    CartItemListAPIView,
    ProductListAPIView, 
    ProductDetailAPIView
)

urlpatterns = [
    # URLs cho trang web
    path('', home, name='home'),
    path('cart/', cart_page, name='cart_page'),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    
    # URLs cho API cũ
    path('api/add-to-cart/', add_to_cart_api, name='add_to_cart_api'),
    path('api/cart-items/', CartItemListAPIView.as_view(), name='cart_item_list_api'),

    # BẠN BỊ THIẾU 2 DÒNG NÀY CHO API SẢN PHẨM MỚI
    path('api/products/', ProductListAPIView.as_view(), name='product-list-api'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail-api'),
]