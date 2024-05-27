from django.shortcuts import render, get_object_or_404

from products.models import Product, ProductReview


# Create your views here.
def home_page(request):
    products = Product.objects.all()
    search_query = request.GET.get('q', '')
    if search_query:
        products = products.filter(name__icontains=search_query)
    context = {'products': products}
    return render(request, 'index.html', context)


def detail_page(request, slug):
    if request.method == "POST":
        product = get_object_or_404(Product, slug=slug)
        review = request.POST.get('review')
        user = request.user
        ProductReview.objects.create(user=user, product=product, review=review)

    product = get_object_or_404(Product, slug=slug)
    product_reviews = ProductReview.objects.all().order_by('-created_at').filter(product=product)
    context = {'product': product, 'product_reviews': product_reviews}
    return render(request, 'product_detail.html', context)
