from .models import product
from django import forms

class prod_form(forms.ModelForm):
    class Meta:
        model=product
        fields=('image',)