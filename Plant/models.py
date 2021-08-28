from django.db import models

# Create your models here.

class Plant(models.Model):
    plant_name = models.CharField(max_length=100, default="")
    price = models.IntegerField(blank=True)
    picture = models.ImageField(upload_to='images/plants/',blank=True)

    def __str__(self):
        return self.plant_name
