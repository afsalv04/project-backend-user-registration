from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField()
    phone = models.IntegerField()
    address = models.CharField()
    city = models.CharField()
    state = models.CharField()
    pincode = models.IntegerField()


class product(models.Model):
     product_id = models.IntegerField()
     name = models.CharField(max_length=100)
     brand = models.CharField()
     category = models.CharField()
     price = models.IntegerField()
     size = models.IntegerField()
     color = models.CharField()
     stock = models.IntegerField()
     image = models.ImageField()






class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.user.get_full_name() or self.user.username



    
# def __str__(self):
#         return self.name