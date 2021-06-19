from typing import DefaultDict
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class cart(models.Model):
    Cart_id=models.AutoField(primary_key=True)
class customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,default="", on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=20,null =  False,default="")
    address=models.CharField(max_length=20, null = False)
    pincode=models.IntegerField(null=False)
    phone_number=models.IntegerField(null=False)  
    def __str__(self):
        return self.customer_name
class seller(models.Model):
    user=models.OneToOneField(User,default="", on_delete=models.CASCADE)
    name=models.CharField(max_length=20,null=False)
    address=models.CharField(max_length=10,null=False)
    phone_num=models.IntegerField(null=False)
    def __str__(self):
        return self.name

class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=50, null = False)
    product_disc = models.CharField(max_length=200, null = False,default="")
    product_details = models.CharField(max_length=200, null = False,default="")
    date = models.DateField(default=timezone.now(), null = False)
    product_price = models.IntegerField(null = False)
    product_commission = models.IntegerField(null = False,default=0)
    product_size = models.CharField(max_length=2,null = False)
    product_gender = models.CharField(max_length=1,null = False,default="F")
    quantity=models.IntegerField(null = False)
    image=models.ImageField(upload_to='shop/images',default="")
    seller=models.ForeignKey(seller,on_delete=models.CASCADE)
    def __str__(self):
        return self.product_title

class payment(models.Model):
    payment_id=models.CharField(max_length=10,primary_key=True)
    payment_date=models.DateField(max_length=10,null=False)
    payment_type=models.CharField(max_length=10,null=False)
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    cart_id=models.ForeignKey(cart,on_delete=models.CASCADE)
class cart_items(models.Model):
    qty=models.IntegerField(max_length=2,null=False)
    date_added=models.DateField(null=False)
    cart_id=models.ForeignKey(cart,on_delete=models.CASCADE)
    product_id=models.ForeignKey(products,on_delete=models.CASCADE)
    cart_id=models.ForeignKey(cart,on_delete=models.CASCADE)



