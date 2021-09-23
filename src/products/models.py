from typing import DefaultDict
from django.db import models

# Create your models here.
#in this case my products will be trucks 

class product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to ='products', default='no_picture.jpg')
    price = models.FloatField(help_text='ksh ')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


##this string rep product and date created
    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d/%m/%y')}"



