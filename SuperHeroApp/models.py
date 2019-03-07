from django.db import models

# Create your models here.

# (Flight, Speed, Invisibility, Telekenetic, Healing, Other)
#
# (Good, kinda good, neutral, a little evil, evil)


class SuperHeroModel(models.Model):
    Name = models.CharField(max_length=100,default='')
    HomeLocation = models.CharField(max_length=100,default='')
    RichOrPower = models.CharField(max_length=100,default='')
    Power= models.CharField(max_length=100,default='')
    Alignment = models.CharField(max_length=100,default='')
    PowerUsageExample = models.TextField(max_length=500,default='')