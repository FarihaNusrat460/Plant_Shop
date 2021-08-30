from django.db import models
from django.contrib.auth.models import User
from Plant.models import Plant
from Equipment.models import Equipment

# Create your models here.
class Order(models.Model):
    plant_name = models.CharField(max_length=100, default="",blank=True)
    equipment_name = models.CharField(max_length=100, default="",blank=True)
    price = models.IntegerField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.plant_name
