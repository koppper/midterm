from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    is_manager = models.BooleanField(default=False)
    image = models.ImageField(upload_to="staff/imgs/", blank=True, null=True)

    def __str__(self):
        return self.name
