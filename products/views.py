from django.shortcuts import render, get_object_or_404

from products.models import Product


# Create your views here.
def home_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def detail_page(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
