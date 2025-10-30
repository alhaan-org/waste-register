from django.db import models
from django.db.models import Sum, F, ExpressionWrapper

# Create your models here.
class Warehouse(models.Model):
    owner = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE, related_name="warehouse_owner")
    manager = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE, related_name="warehouse_manager")
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255)
    gst_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"

    def __str__(self):
        return f"{self.name} -> Owner: {self.owner}"

    def total_revenue(self):
        t_revenue = self.items.filter(is_sold=True).aggregrate(
            total = Sum('sold_price')
        )['total'] or 0
        return t_revenue

    def total_profit(self):
        total_profit_expr = ExpressionWrapper(
            F('sold-price') - F('cost-price'),
            output_field = models.DecimalField(max_digits=15, decimal_places=2)
        )
        profit = self.items.filter(is_sold=True).aggregate(
            total = Sum(total_profit_expr)
        )['total'] or 0
        return profit

    def profit_percentage(self):
        return (self.total_profit() / self.total_revenue()) * 100


class Item(models.Model):
    ITEM_TYPE = (
        ('computer', 'Computer Scrap'),
        ('tv', 'LCD, LED, TV Screens'),
        ('mobile', 'Mobile Scrap'),
        ('radio', 'Radio Device'),
        ('medical', 'Medical Equipments Scrap Item'),
        ('electronic', 'Electronic Items')
    )
    product_name = models.CharField(max_length=100, blank=False)
    item_code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=50, choices=ITEM_TYPE, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sold_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_sold = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_sold = models.DateTimeField(null=True, blank=True)

    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="items")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ["-date_added"]

    def __str__(self):
        return f"{self.product_name} -> {self.type}"

    def profit_margin(self):
        if self.cost_price and self.sold_price:
            return round(self.sold_price - self.cost_price, 2)
        return None

