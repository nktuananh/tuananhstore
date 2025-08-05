from django.urls import path
from .views import add_to_cart, cart_page, update_quantity, checkout, delete_item, web_page
from .views import web_page 
from .views import ProductListAPIView


urlpatterns = [
    path('add/', add_to_cart, name='add_to_cart'),
    path('', cart_page, name='cart_page'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
    path('update/<int:item_id>/', update_quantity, name='update_quantity'),
    path('checkout/', checkout, name='checkout'),
    path('web/', web_page, name='web_page'),
]

api_urlpatterns = [
    path('api/products/', ProductListAPIView.as_view(), name='product-list-api'),
]
urlpatterns += api_urlpatterns