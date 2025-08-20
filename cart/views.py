# cart/views.py

# === KHU VỰC IMPORT ===
# (Tất cả import được đặt gọn gàng ở đầu file)
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
import json

from rest_framework import generics

from .models import Product, CartItem 
from .serializers import ProductSerializer, CartItemSerializer
from .forms import AddToCartForm


# === CÁC VIEW DÀNH CHO TRANG WEB (RENDER HTML) ===

def home(request):
    """Hiển thị trang chủ với danh sách sản phẩm."""
    products = Product.objects.all()
    return render(request, 'cart/home.html', {'products': products})


def cart_page(request):
    """Hiển thị trang giỏ hàng."""
    items = CartItem.objects.all().order_by('-added_at')
    total = sum(item.get_total_price() for item in items) 
    return render(request, 'cart/cart.html', {
        'items': items,
        'total': total
    })


def product_detail_view(request, product_id):
    """Hiển thị trang chi tiết của một sản phẩm."""
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm()
    context = {
        'product': product,
        'form': form
    }
    return render(request, 'cart/product_detail.html', context)


# === CÁC VIEW DÀNH CHO API (TRẢ VỀ JSON) ===

@csrf_exempt 
def add_to_cart_api(request):
    """API để thêm sản phẩm vào giỏ hàng từ frontend."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data['product_id']
            product = get_object_or_404(Product, id=product_id)

            cart_item, created = CartItem.objects.get_or_create(
                product=product,
                size=data['size'],
                defaults={'quantity': data.get('quantity', 1)}
            )

            if not created:
                cart_item.quantity += data.get('quantity', 1)
                cart_item.save()

            return JsonResponse({'message': 'Đã cập nhật giỏ hàng!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Yêu cầu không hợp lệ'}, status=405)


class ProductListAPIView(generics.ListCreateAPIView):
    """API để lấy danh sách TẤT CẢ sản phẩm."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
#----------------------------------

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """API để lấy/sửa/xóa CHI TIẾT của 1 sản phẩm."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# ---------------------------------


class CartItemListAPIView(generics.ListAPIView):
    """API để lấy danh sách các món hàng trong giỏ."""
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer