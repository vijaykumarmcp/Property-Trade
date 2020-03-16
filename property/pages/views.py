from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listings
from listings.choices import bedroom_choices,price_choices,state_choices
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings=Listings.objects.order_by('-list_date').filter(is_published=True)[:3]

    context={
        'listings':listings,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices
    }
    return render(request, 'pages/index.html',context)

def about(request):
    realtors=Realtor.objects.all()

    context={
        'realtors':realtors
    }
    return render(request, 'pages/about.html',context)

