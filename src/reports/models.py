from django.db import models
from django.db.models.deletion import CASCADE
from profiles.models import  profile


class Report(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to = 'reports', blank = True)
    remarks = models.TextField()
    author = models.ForeignKey(profile, on_delete= CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def  __str__(self):
        return str(self.name)