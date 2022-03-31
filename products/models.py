from django.db import models

class Product(models.Model):
  name = models.CharField(max_length = 50, blank = False)
  description = models.TextField(blank = True)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  minimum_age_appropriate = models.IntegerField(default = 0, blank = False)
  maximum_age_appropriate = models.IntegerField(default = -1, blank = False)
  
  def __str__(self):
    return f"{self.name} ${self.price}" 
   
  # Create your models here.
