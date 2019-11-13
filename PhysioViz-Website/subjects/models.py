from django.db import models

# Create your models here.

class subject(models.Model):
    subject_number  = models.IntegerField(default=0) 
    age             = models.IntegerField(default=0)  
    gender          = models.CharField(max_length=1)
    height_cm       = models.FloatField()
    weight_kg       = models.FloatField()   

    