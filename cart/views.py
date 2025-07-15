from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import CartItem
import json


def home(request):
    return HttpResponse("<h1>Chào mừng đến với Tuấn Anh Store</h1>")


def cart_page(request):
    items = CartItem.objects.all().order_by('-added_at')
    total = sum(item.price * item.quantity for item in items)
    return render(request, 'cart/cart.html', {
        'items': items,
        'total': total
    })


@csrf_exempt
def update_quantity(request, item_id):
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity'))
            item = CartItem.objects.get(id=item_id)
            item.quantity = quantity
            item.save()
        except:
            pass
    return redirect('cart_page')


@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'POST':
        CartItem.objects.filter(id=item_id).delete()
    return redirect('cart_page')


@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        CartItem.objects.all().delete()
        return render(request, 'cart/thank_you.html')
    return redirect('cart_page')


@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            item = CartItem.objects.create(
                name=data['name'],
                price=data['price'],
                image=data['image'],
                size=data['size'],
                quantity=data.get('quantity', 1)
            )

            return JsonResponse({'message': 'Đã thêm vào giỏ hàng!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif request.method == 'GET':
        items = CartItem.objects.all().order_by('-added_at')
        data = [{

            'name': item.name,
            'price': item.price,
            'image': item.image,
            'size': item.size,
            'quantity': item.quantity,
            'added_at': item.added_at.strftime('%Y-%m-%d %H:%M:%S')
        } for item in items]

        return JsonResponse({'cart': data})

    else:
        return JsonResponse({'error': 'Chỉ hỗ trợ POST và GET'})
    
from django.shortcuts import render

def web_page(request):
    return render(request, 'cart/web.html')

