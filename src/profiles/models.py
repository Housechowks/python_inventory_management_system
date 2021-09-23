from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class profile(models.Model):
    # to make sure user has only one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bios....")
    avatar = models.ImageField(upload_to= 'avatars', default = 'no_picture.jpg')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"profile of {self.user.username}"

