from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Business,NeighborHood,Userprofile,Post,PoliceCenters,HealthCenter,Comment
from .forms import NewProfileForm,NewNeighborhoodForm,UpdateForm,NewPostForm,NewBusinessForm,NewCommentForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def homepage(request):

    businesses=Business.get_all_businesses()
    neighborhoods=NeighborHood.get_all_neighborhoods()
    posts=Post.get_all_posts()

    current_user=request.user
    if request.method == 'POST':
        form =NewCommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)

            comment.commenter = current_user

            comment.save()
        return redirect('homepage')
    else:
        form=NewCommentForm()


    return render(request,'homepage.html',{"businesses":businesses,"neighborhoods":neighborhoods,"posts":posts,"form":form})


def comments(request):

    comments=Comment.get_comments()

    return render(request,'comments.html',{"comments":comments})

def new_comment(request):
    current_user=request.user
    if request.method == 'POST':
        form =NewCommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)

            comment.commenter = current_user

            comment.save()
        return redirect('homepage')
    else:
        form=NewCommentForm()
    return render(request,'comment.html',{"form":form})


def contacts(request):
    police=PoliceCenters.get_all_police()
    health=HealthCenter.get_all_health()
#
    return render(request,'contact.html',{"police":police,"health":health})

def neighbourhood(request,neighborhood_id):
    businesses=Business.objects.filter(neighborhood_id=neighborhood_id)



def neighborhood(request,neighborhood_id):
    neighborhood=NeighborHood.objects.get(id=neighborhood_id)

    return render(request,'neighborhood.html',{"neighborhood":neighborhood})



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




def business(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewBusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business=form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('homepage')
    else:
        form=NewBusinessForm()
    return render(request,'business.html',{"form":form})



def profile(request):
    current_user=request.user
    userprofile = Userprofile.objects.filter(user_name=current_user)

    if len(userprofile)<1:
        userprofile = "No profile"
    else:
        userprofile = Userprofile.objects.get(user_name=current_user)
    return render(request,'profile.html',{"userprofile":userprofile})


def edit_profile(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            userprofile=form.save(commit=False)
            userprofile.user_name = current_user
            userprofile.save()
        return redirect('profile')
    else:
        form=NewProfileForm()
    return render(request,'edit_profile.html',{"form":form})





def update_neighborhood(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewNeighborhoodForm(request.POST,request.FILES)
        if form.is_valid():
            userprofile=form.save(commit=False)
            userprofile.user_name = current_user
            userprofile.save()
        return redirect('profile')
    else:
        form=NewNeighborhoodForm()
    return render(request,'update_neighborhood.html',{"form":form})




def update_profile(request,id):
    instance=get_object_or_404(Userprofile,id=id)
    form=UpdateForm(request.POST or None,instance=instance)
    if form.is_valid():
        form.save
        return redirect('profile')

    return render(request,'update_profile.html', {'form': form})





def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_business_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def businessdetails(request,business_id):

    business=Business.objects.get(id=business_id)

    return render(request,"businessdetails.html",{"business":business})
