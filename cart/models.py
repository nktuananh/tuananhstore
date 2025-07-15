from django.db import models

class CartItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - Size {self.size} x{self.quantity}"
