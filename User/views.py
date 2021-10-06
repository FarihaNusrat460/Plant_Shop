from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from Product.models import Cart
from django.contrib.auth.models import User
# Create your views here.

def registration(request):
    #creating an empty form for user registration
    form = UserCreationForm()

    # after submit button in the HTML page
    if request.method == "POST":
        # filling out the form with the inserted data from HTML page
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # if valid then save to database
            user = form.save()
            messages.success(request, 'Account is created successfully')
            # create a new cart for new user
            cart = Cart(user = user)
            cart.save()

            # after a successful registration you can redirect to any page
            return redirect('Product')

    context={
        'form' : form
    }

    return render(request, 'User/registration.html', context)
