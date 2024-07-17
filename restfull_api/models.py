from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    bio = models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
