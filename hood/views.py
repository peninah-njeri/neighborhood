from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    businesses=Business.get_all_businesses()
    neighborhoods=NeighborHood.get_all_neighborhoods()

    return render(request,'homepage.html',{"businesses":businesses,"neighborhoods":neighborhoods})