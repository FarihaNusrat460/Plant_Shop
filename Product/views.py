from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Product,Order,Cart
from .forms import  ReviewForm

from django.contrib.auth.decorators import login_required




# Create your views here.

def showProducts(request):

    products = Product.objects.all()
    if request.method == 'POST':
        products= Product.objects.filter(plant_name__icontains=request.POST['search'])


    context = {
        'all_products':products

    }

    return render(request,'Product/show_product.html',context)

def showHome(request):
    return render(request, 'Homepage/show_homepage.html')


def showDetails(request, product_id):

    searched_product = get_object_or_404(Product, id=product_id)

    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            searched_product.reviews.add(instance)
            searched_product.save()

    context = {
        'search': searched_product,
        'form': form
    }
    return render(request, 'Product/show_product_details.html', context)


def showDetails2(request, product_id):

    #searched_product = get_object_or_404(Product, id=product_id)

    #searched_product = Product.objects.get(id=product_id) #sure one return
    #print(searched_product)

    searched_plant = Product.objects.filter(id=product_id)  # many return

    #searched_product = get_object_or_404(Product, id=product_id)
    #print(searched_product)



    if len(searched_plant) == 0:
        does_exists = False
        context = {
            'does_exists': does_exists,
        }
    else:
        does_exists = True
        search = searched_plant[0]
        context = {
            'does_exists': does_exists,
            'search': search
        }

    return render(request, 'Plant/show_product_details.html', context)


@login_required
def make_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order = Order(user=request.user, product=product)
    order.save()
    print("Order done!")

    cart = Cart.objects.get(user=request.user)
    cart.product.remove(product)
    cart.save()
    print("Remove done!")

    return redirect('cart')


def test(request):
    print(request.POST)

    return redirect('Product')


def bkash_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order = Order(user=request.user, product=product)
    order.transaction_id = request.POST['transaction_id']
    order.payment_options  = 'Bkash'
    order.save()

    cart = Cart.objects.get(user=request.user)
    cart.product.remove(product)
    cart.save()

    #return HttpResponseRedirect(reverse('cart'))
    return redirect('cart')

@login_required
def view_cart(request):
    cart = Cart.objects.get(user=request.user)


    total = 0
    for product in cart.product.all():
        total += product.price

    context = {

        'cart':cart,
        'product': product,

        'total' : total
    }

    return render(request, 'Product/cart.html', context)

@login_required
def update_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)

    cart.product.add(product)
    cart.save()

    return redirect('cart')

'''
try:
    cart = Cart.objects.get(user=request.user)
except cart.DoesNotExist:
    cart = Cart(user=request.user)
'''


@login_required
def delete_from_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(user=request.user)

    cart.product.remove(product)
    cart.save()

    return redirect('cart')

@login_required
def make_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order = Order(user=request.user, product=product)
    order.save()
    print("Order done!")

    cart = Cart.objects.get(user=request.user)
    cart.product.remove(product)
    cart.save()
    print("Remove done!")

    return redirect('cart')


def test(request):
    print(request.POST)

    return redirect('Product')

@login_required
def my_orders(request):
    orders = Order(user=request.user)

    try:
        orders = Order.objects.filter(user=request.user)
        order_status = True
    except orders.DoesNotExist:
        orders = Order(user=request.user)
        order_status = False

    total = 0.0
    for order in orders:
        total += order.product.price

    context = {
        'orders': orders,
        'order_status': order_status,
        'total': total

    }
    return render(request, 'Product/order.html', context)