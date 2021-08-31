from django.db import models

# Create your models here.

class Equipment(models.Model):
    equipment_name = models.CharField(max_length=100, default="")
    price = models.IntegerField(blank=True)
    picture = models.ImageField(upload_to='images/equipments/',null=True,blank=True)

    def __str__(self):
        return self.equipment_name



