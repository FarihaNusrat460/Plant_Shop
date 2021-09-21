from django.shortcuts import render
from .models import Equipment
# Create your views here.

def showEquipmenmts(request):

    equipments = Equipment.objects.all()

    context = {
        'all_equipments':equipments

    }

    return render(request,'Equipment/show_equipment.html',context)
