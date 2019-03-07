from django.db import models

# Create your models here.

# (Flight, Speed, Invisibility, Telekenetic, Healing, Other)
#
# (Good, kinda good, neutral, a little evil, evil)
# power choices for a dropdown

Power_Choices = \
    (
        ('flight','Flight'),
        ('speed','Speed'),
        ('invisibility','Invisibility'),
        ('telekinesis','Telekinesis'),
        ('healing','Healing'),
        ('other','Other'),
    )

class SuperHeroModel(models.Model):
    Name = models.CharField(max_length=100,default='')   #all fields use char field for now and are modified if necessary in forms page
    HomeLocation = models.CharField(max_length=100,default='')
    RichOrPower = models.CharField(max_length=100,default='')
    Power= models.CharField(max_length=100,default='',choices=Power_Choices) #add choices for a dropdown field
    Alignment = models.CharField(max_length=100,default='')
    PowerUsageExample = models.TextField(max_length=500,default='')