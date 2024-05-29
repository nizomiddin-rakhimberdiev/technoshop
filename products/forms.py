from django import forms

from products.models import ProductReview


class EditReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('review',)