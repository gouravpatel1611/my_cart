from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.
class Product(models.Model):
    Product_id = models.AutoField
    Product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50 , default="")
    sub_category = models.CharField(max_length=50 , default="")
    desc = models.CharField(max_length=70)
    model = models.CharField(max_length=50, default="")
    color = models.CharField(max_length=10, default="default color")
    price = models.IntegerField(default=0)
    image = ImageField(upload_to="shop/images", default="")
    pub_date = models.DateField()
    
    def __str__(self):
        return self.Product_name


class Contect(models.Model):
    msg_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50 , default="")
    email = models.CharField(max_length=50 , default="")
    comment = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.fname




class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models,CharField(max_length=5000)
    first_name = models.CharField(max_length=90, default="" )
    last_name = models.CharField(max_length=90, default="" )
    phone = models.CharField(max_length=90, default="" )
    email = models.CharField(max_length=90)
    address1 = models.CharField(max_length=500,default="")
    address2 = models.CharField(max_length=500,default="")
    state = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    pin_code = models.CharField(max_length=90)
    address_for_next_time = models.CharField(max_length=100,default="" )

    