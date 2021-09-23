from django.db import models
from django.db.models.deletion import CASCADE
from products.models import product
from customers.models import custmer
from profiles.models import profile
from django.utils import timezone
from .utills import generate_code
from django.shortcuts import reverse



# Create your models here.
class Position(models.Model):
    Product = models.ForeignKey(product, on_delete=CASCADE)
    Quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.Product.price * self.Quantity
        return super().save(*args, **kwargs)

    def get_sales_id(self):
        sale_obj = self.sale_set.first()
        return sale_obj.id


    def __str__(self):
        return f" id: {self.id}, product: {self.Product.name}, quantity:{self.Quantity}  "



class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(custmer, on_delete=CASCADE)
    salesman = models.ForeignKey(profile, on_delete=models.CASCADE)
    created = models.DateField(blank=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"sales for amount of ksh {self.total_price}"

    def get_absolute_url(self):
        return reverse( 'sales:detail', kwargs = { 'pk' : self.pk} )

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
           self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_created=True)

    def __str__(self):
        return str(self.file_name)

