from django.forms import ModelForm
from .models import Review, ReviewDetail


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'review', 'rating',   )

class ReviewDetailForm(ModelForm):
    class Meta:
        model = ReviewDetail
        fields = ('detail',   )