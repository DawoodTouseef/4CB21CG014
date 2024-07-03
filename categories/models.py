from django.db import models


class Companies(models.Model):
    name=models.CharField(max_length=520,unique=True)
    def __str__(self) -> str:
        return self.name
    
# Create your models here.
class Categoris(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE)
    name=models.CharField(max_length=5852,unique=True)
    def __str(self):
        return self.name

class Product_table(models.Model):
    categoris=models.ForeignKey(Categoris,on_delete=models.CASCADE)
    product_name=models.TextField(max_length=25630)
    price=models.IntegerField()
    rating=models.IntegerField()
    discount=models.IntegerField()
    availability=models.BooleanField()
