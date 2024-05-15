from django.db import models

# Create your models here.
class product_tbl(models.Model):
    property_name = models.CharField(max_length=200)
    property_type = models.CharField(max_length=50,null=True)
    dimension = models.CharField(max_length=50,null = True)
    price = models.IntegerField(null= True)
    address = models.CharField(max_length = 500)
    possession = models.CharField(max_length = 50,null= True)
    description = models.CharField(max_length = 500)
    property_image1=models.FileField(upload_to='pictures')
    property_image2=models.FileField(upload_to='pictures',null=True,blank=True)
    property_image3=models.FileField(upload_to='pictures',null=True,blank=True)
    property_image4=models.FileField(upload_to='pictures',null=True,blank=True)
    property_image5=models.FileField(upload_to='pictures',null=True,blank=True)
    property_image6=models.FileField(upload_to='pictures',null=True,blank=True)
    property_image7=models.FileField(upload_to='pictures',null=True,blank=True)
    property_image8=models.FileField(upload_to='pictures',null=True,blank=True)

    def __str__(self):
        return self.property_name
class Seller(models.Model):
    name=models.TextField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    password=models.TextField(max_length=100)
    