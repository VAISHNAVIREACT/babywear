from django.db import models

# Create your models here.



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)  # Add title field
    image = models.ImageField(upload_to='product_images/')  # Add image field
    description = models.TextField()  # Add description field
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as needed

    def __str__(self):
        return self.title

# class Product(models.Model):
#     name = models.CharField(max_length=40)
#     product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField for accurate price representation
#     description = models.CharField(max_length=500)
#     title = models.CharField(max_length=100)  # Add title field
#     image = models.ImageField(upload_to='product_images/')  # Add image field

#     def __str__(self):
#         return self.name



class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address=models.TextField()
    mobile = models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.name


class TrackingDetail(models.Model):
    date=models.DateField()
    location=models.CharField( max_length=50)
    status=models.CharField( max_length=100)

