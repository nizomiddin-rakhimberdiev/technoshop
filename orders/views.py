from django.shortcuts import get_object_or_404, render, redirect

from orders.models import Order
from products.models import Product


def create_order(request, slug):
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=slug)
        quantity = int(request.POST['quantity'])
        address = request.POST['address']
        Order.objects.create(user=request.user, product=product, quantity=quantity, address=address)
        return redirect('products:index')
    else:
        product = get_object_or_404(Product, slug=slug)
    return render(request, 'create_order.html', {'product': product})