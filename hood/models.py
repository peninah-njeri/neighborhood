from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NeighborHood(models.Model):
    neighborhood_image=models.ImageField(upload_to='neighborhoods',null=True)
    name=models.CharField(max_length =40)
    location=models.CharField(max_length=40)
    occupants_count=models.PositiveIntegerField(blank=True,null=True)


    def __str__(self):
        return self.name


class Userprofile(models.Model):
    profile_image=models.ImageField(upload_to='userprofiles',null=True)
    user_name=models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "user")
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)



class Business(models.Model):
    business_image=models.ImageField(upload_to='businesses',null=True)
    business_name=models.CharField(max_length =30)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)    


class Post(models.Model):
    post_image=models.ImageField(upload_to='posts',null=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length =30)
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    post=models.TextField()

def __str__(self):
        return self.title
   


class HealthCenter(models.Model):
    name = models.CharField(max_length = 50)
    location=models.CharField(max_length =50)
    contact=models.CharField(max_length=40)


class PoliceCenters(models.Model):
    name = models.CharField(max_length = 50)
    location=models.CharField(max_length =50)
    contact=models.CharField(max_length=40)



class Comment(models.Model):
    post = models.ForeignKey(Post,blank=True, on_delete=models.CASCADE,null=True,related_name='comment')
    commenter=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    comment=models.TextField(max_length =30)



class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Location(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name
