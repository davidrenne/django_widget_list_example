from django.db import models

# Create your models here.
class Item(models.Model):
    name        = models.CharField(max_length=50) 
    price       = models.DecimalField(decimal_places=2,max_digits=10) 
    sku         = models.IntegerField() 
    active      = models.CharField(max_length=3,default='Yes') 
    date_added  = models.DateField() 
    def __unicode__( self ):
        return "Item: " + self.name + "(" + str(self.id) + ")"
