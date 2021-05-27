from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from cart.utils.cart import Cart
from orders.models import Order, OrderItem


@login_required()
def order_create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    # cart.clear()
    return redirect('orders:detail', order.id)


@login_required()
def detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order.html', {'order': order})
