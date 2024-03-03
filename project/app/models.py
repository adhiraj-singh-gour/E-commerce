from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Message = models.CharField(max_length=200)

class Products(models.Model):
    Name = models.CharField(max_length=20)
    Type = models.CharField(max_length=20)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", height_field=None,width_field=None,max_length=100)


class Signup(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    Cpassword = models.CharField(max_length=30)


class ItemModel(models.Model):
    name = models.CharField(max_length = 100)
    amount = models.IntegerField()
    order_id = models.CharField(max_length = 100)
    razorpay_payment_id = models.CharField(max_length = 100,blank=True)
    paid = models.BooleanField(default=False)