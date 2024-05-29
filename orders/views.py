from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from products.models import Product
from .models import Order, OrderItem
from .forms import OrderForm

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item_id, quantity in request.POST.items():
                if item_id.startswith('product_'):
                    product_id = int(item_id.split('_')[1])
                    product = Product.objects.get(id=product_id)
                    OrderItem.objects.create(order=order, product=product, quantity=quantity)
            return redirect('products:index')
    else:
        form = OrderForm()
    return render(request, 'order_create.html', {'form': form})

# Boshqa buyurtmalar va sotishlar bo'yicha funksiyalar kerak bo'lsa, ularni qo'shing
