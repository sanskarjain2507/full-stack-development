from django.db import models

# Create your models here.

class product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    pub_date = models.DateField(default="2019-12-22")
    image=models.ImageField(upload_to="shop/images")

    def __str__(self):
        return self.product_name

    class Meta:
        db_table="products"

