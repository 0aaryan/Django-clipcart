from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms.widgets import Widget
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import views as auth_views
from .models import customer, products,seller


class CustomerRegistration(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))


class Meta:
    model = User
    fields = ['username' 'email', 'password1', 'password2']
    labels = {'email': 'Email'}
    widgets = {'username': forms.TextInput(attrs={"class": "form-control"})}


class Loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class CustomerProfileForm(forms.ModelForm):

    class Meta:

        model = customer
        fields = ['customer_name', 'address', 'pincode', 'phone_number']
        widgets = {'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
                  'address': forms.TextInput(attrs={'class': 'form-control'}), 
                  'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
                  'pincode': forms.NumberInput(attrs={'class': 'form-control'})
                   }
class SellerProfileForm(forms.ModelForm):

    class Meta:

        model = seller
        fields = ['name', 'address', 'phone_num']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone_num': forms.NumberInput(attrs={'class': 'form-control'}),
                   }

class ProductAddForm(forms.ModelForm):

    class Meta:

        model = products
        fields = [
            'product_title',
            'product_disc',
            'product_details',
            'date',
            'product_price',
            'product_commission',
            'product_size',
            'product_gender',
            'quantity',
            'image',
        ]
    
