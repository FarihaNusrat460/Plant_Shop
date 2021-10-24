
from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect

from .models import Product,Cart,Order,Review

from django.contrib.auth.decorators import login_required

from .forms import ProductForm, ReviewForm

# Create your views here.

def showProducts(request):

    products = Product.objects.all()
    if request.method == 'POST':
        products= Product.objects.filter(product_name__icontains=request.POST['search'])


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


    searched_product = Product.objects.filter(id=product_id)  # many return


    if len(searched_product) == 0:
        does_exists = False
        context = {
            'does_exists': does_exists,
        }
    else:
        does_exists = True
        search = searched_product[0]
        context = {
            'does_exists': does_exists,
            'search': search
        }

    return render(request, 'Product/show_product_details.html', context)


@login_required
def uploadProducts(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid:
            form.save()
            return redirect('Product')

    context = {
        'form' : form
    }

    return render(request, 'Product/upload.html', context)

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


def view_cart(request):

    cart = Cart.objects.get(user=request.user)

    total = 0
    for product in cart.product.all():
         total += product.price

    context = {

        'cart':cart,
        # 'plant':plant,

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
def review_after_complete(request, product_id):

    already_reviewed = False

    searched_product = get_object_or_404(Product, id=product_id)

    user_list = searched_product.reviews.filter(user=request.user)
    print(user_list, len(user_list))
    if len(user_list) != 0:
        already_reviewed = True


    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            searched_product.reviews.add(instance)
            searched_product.save()

            return redirect('my-orders')

    context = {
        'search': searched_product,
        'form': form,
        'already_reviewed': already_reviewed
    }
    return render(request, 'Product/detail_product_view_review.html', context)



