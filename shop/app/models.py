from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=30)
    image = models.ImageField(upload_to='/image',null=True,blank=True)
    price = models.PositiveIntegerField()
    quantity = models.CharField(max_length=30)
    
       
class Order(models.Model):
    order_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30)
    total_money = models.PositiveIntegerField()


class User(models.Model):
    user_name = models.CharField(max_length=255)
    user_orders = models.ForeignKey(Order, on_delete=models.CASCADE) 
    
    
    
    
    
    
    
