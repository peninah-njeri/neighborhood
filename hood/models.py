from django.db import models

# Create your models here.

class NeighbourHood(models.Model):
    name=models.CharField(max_length =40)
    location=models.CharField(max_length=40)
    occupants_count=models.PositiveIntegerField(blank=True,null=True)



class Userprofile(models.Model):
    user_name=models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "user")
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)



class Business(models.Model):
    business_name=models.CharField(max_length =30)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)    

