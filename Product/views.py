from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Product

from django.contrib.auth.decorators import login_required




# Create your views here.

def showProducts(request):

    products = Product.objects.all()
    if request.method == 'POST':
        products= Product.objects.filter(plant_name__icontains=request.POST['search'])


    context = {
        'all_products':products

    }

    return render(request,'Product/show_product.html',context)

def showHome(request):
    return render(request, 'Homepage/show_homepage.html')
