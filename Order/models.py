from django.db import models
from django.contrib.auth.models import User
from Plant.models import Plant
from Equipment.models import Equipment



# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Delivering', 'Delivering'),
        ('Completed', 'Completed')
    )

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')

    PAYMENT_CHOICES = (
        ('Bkash', 'Bkash'),
        ('Rocket', 'Rocket'),
        ('Payment on delivery', 'Payment on delivery')
    )
    payment_options = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='Payment on delivery')
    is_paid = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=30, null=True, blank=True)

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username + "-" + self.plant.plant_name + "-" + self.status

