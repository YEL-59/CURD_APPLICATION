from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)
    varsity_id = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=20) 
    phone = models.CharField(max_length=20) 
    email = models.EmailField()
