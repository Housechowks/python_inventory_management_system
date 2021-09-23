from src.settings import DATABASES
from django.db import models

## model are classes and classes are tables in the DATABASES
#note name customer


class custmer(models.Model):
   name = models.CharField(max_length=120)
   logo = models.ImageField(upload_to='customers', default='no_picture.jpg')

## imply that each customer is resprented by name

def __str__(self):
    return str(self.name)