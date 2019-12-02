from django.shortcuts import render
from django.http import HttpResponse
from .models import Business,NeighborHood,Userprofile,Post,PoliceCenters,HealthCenter,Comment

# Create your views here.
def homepage(request):

    businesses=Business.get_all_businesses()
    neighborhoods=NeighborHood.get_all_neighborhoods()
    posts=Post.get_all_posts()

   
    return render(request,'homepage.html',{"businesses":businesses,"neighborhoods":neighborhoods,"posts":posts})




def business(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewBusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business=form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('index')
    else:
        form=NewBusinessForm()
    return render(request,'business.html',{"form":form})


def post(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.owner = current_user
            post.save()
        return redirect('homepage')
    else:
        form=NewPostForm()
    return render(request,'post.html',{"form":form})


