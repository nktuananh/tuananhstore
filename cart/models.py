# cart/models.py
from django.db import models

# Model mới để lưu thông tin sản phẩm gốc
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    image = models.CharField(max_length=255) # Hoặc ImageField

    def __str__(self):
        return self.name

# Model giỏ hàng bây giờ sẽ gọn hơn rất nhiều
class CartItem(models.Model):
    # Liên kết đến sản phẩm gốc
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    # Thông tin do người dùng chọn
    size = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Size: {self.size})"

    # Hàm để tính tổng giá của mục này
    def get_total_price(self):
        return self.product.price * self.quantity