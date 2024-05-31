from django.shortcuts import render, get_object_or_404, redirect

from products.forms import EditReviewForm, CreateProductForm
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


def edit_review(request, slug, id):
    product = get_object_or_404(Product, slug=slug)
    review = get_object_or_404(ProductReview, id=id, product=product)
    if request.method == "POST":
        form = EditReviewForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:detail', slug=slug)
    else:
        form = EditReviewForm(instance=review)
        context = {'form': form}
    return render(request, 'edit_review.html', context)


def delete_review(request, slug, id):
    review = get_object_or_404(ProductReview, id=id)
    review.delete()
    return redirect("products:detail", slug=slug)


def create_product(request):
    if request.method == "POST":
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:index')
    else:
        form = CreateProductForm()
    return render(request, 'create_product.html', context={'form': form})


