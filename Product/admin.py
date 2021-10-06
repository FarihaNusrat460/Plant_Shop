from django.contrib import admin
from .models import Product,Order,Cart
# Register your models here.


admin.site.register([Product,Order,Cart])