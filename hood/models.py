from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NeighborHood(models.Model):
    name=models.CharField(max_length =40)
    location=models.CharField(max_length=40)
    occupants_count=models.PositiveIntegerField(blank=True,null=True)


    def __str__(self):
        return self.name


class Userprofile(models.Model):
    user_name=models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "user")
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)



class Business(models.Model):
    business_name=models.CharField(max_length =30)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)    


class Post(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length =30)
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    post=models.TextField()