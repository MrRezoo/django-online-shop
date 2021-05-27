from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from cart.forms import Add2CartForm
from cart.utils.cart import Cart
from shop.models import Product
from django.views.decorators.http import require_POST


def detail(request):
    cart = Cart(request)
    return render(request, template_name='cart/detail.html', context={'cart': cart})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = Add2CartForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        cart.add(product=product, quantity=data['quantity'])
    return redirect('cart:detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')
