from django.shortcuts import render
from django.http import HttpResponse
from .models import Business,NeighborHood,Userprofile,Post,PoliceCenters,HealthCenter,Comment

# Create your views here.
def homepage(request):

    businesses=Business.get_all_businesses()
    neighborhoods=NeighborHood.get_all_neighborhoods()
    posts=Post.get_all_posts()

   
    return render(request,'homepage.html',{"businesses":businesses,"neighborhoods":neighborhoods,"posts":posts})


