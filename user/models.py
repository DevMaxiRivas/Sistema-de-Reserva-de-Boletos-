from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    image = models.ImageField(default="default.png", upload_to="profile_images")

    def __str__(self):
        return f"{self.customer.username}-Profile"
