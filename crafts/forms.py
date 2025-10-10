from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'description']
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label="Ism", max_length=50)
    last_name = forms.CharField(label="Familiya", max_length=50)
    phone = forms.CharField(label="Telefon", max_length=20)
    message = forms.CharField(label="Izoh", widget=forms.Textarea, required=False)
