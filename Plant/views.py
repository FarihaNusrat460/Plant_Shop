from django.shortcuts import render
from .models import Plant
# Create your views here.

def showPlants(request):

    plants = Plant.objects.all()

    context = {
        'all_plants':plants

    }

    return render(request,'Plant/show_plant.html',context)

def showHome(request):
    return render(request, 'Homepage/show_homepage.html')