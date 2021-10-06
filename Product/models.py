from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    RATING_OPTIONS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    rating = models.CharField(max_length=10, choices = RATING_OPTIONS, default='4')
    comment = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.rating

class Product(models.Model):
    product_name = models.CharField(max_length=100, default="")
    price = models.IntegerField(blank=True)
    picture = models.ImageField(upload_to='images/plants/',blank=True)
    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.product_name




class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

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

    transaction_id = models.CharField(max_length=30, null =True, blank=True)

    def __str__(self):
        return self.user.username + "-" + self.product.product_name + "-" + self.status

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)  # can be blank or null by default
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username

