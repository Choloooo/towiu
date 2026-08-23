from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Hat(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hats/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Discount percentage (0-100)",
    )

    @property
    def final_price(self):
        """Price after discount"""
        if self.discount > 0:
            return round(self.price - (self.price * self.discount / 100), 2)
        return self.price

    @property
    def has_discount(self):
        return self.discount > 0

    def __str__(self):
        return self.name



class CartItem(models.Model):
    hat = models.ForeignKey('Hat', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.hat.name}"

    @property
    def total_price(self):
        return self.quantity * self.hat.final_price