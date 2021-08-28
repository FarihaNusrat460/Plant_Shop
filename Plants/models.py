from django.db import models

# Create your models here.

class Plants(models.Model):
    plants_name = models.CharField(max_length=100, default="")
    price = models.IntegerField(blank=True)
    picture = models.ImageField(upload_to='images/equipments/',blank=True)

    def __str__(self):
        return self.plants_name
