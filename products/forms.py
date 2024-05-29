from django import forms

from products.models import ProductReview, Product


class EditReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('review',)


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'product_image', 'category')