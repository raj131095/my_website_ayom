from django import forms
from .models import UploadedImage

class UploadImageForm(forms.ModelForm):
    products=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Product details'}))
    class Meta:
        model=UploadedImage
        fields=['title', 'image','price','products']

