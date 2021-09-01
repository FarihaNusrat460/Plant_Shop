from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
# Create your views here.


def registration(request):
    user_form = UserCreationForm()
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Account is created successfully')

    context = {
        'form': user_form,
    }

    return render(request, 'User/registration.html', context)