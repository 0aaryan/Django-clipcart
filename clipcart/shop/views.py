
from django import forms
from django import views
from django.shortcuts import render,HttpResponse
from django.views import View
from . import models
from .forms import CustomerRegistration,CustomerProfileForm,SellerProfileForm,ProductAddForm
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.models import Group

# Create your views here.
def index(request):
    products= models.products.objects.all()
    params={'product':products}  
    return render(request,'shop/home.html',params)
def about(request):
    return render(request,'shop/about.html')
def products(request):
    products= models.products.objects.all()
    n= len(products)
    params={'range':range(1,n), 'product': products}
    return render(request,'shop/products.html',params)
    
def cart(request):
    return render(request,'shop/cart.html')
def login(request):
    return render(request,'shop/login.html')

def productview(request,product_id):
    product= models.products.objects.filter(product_id=product_id)
    return render(request,'shop/productview.html',{'product':product[0]})
class profileview(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'shop/profile.html',{'form':form}) 
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            customer_name = form.cleaned_data[ 'customer_name']
            address = form.cleaned_data['address']
            pincode= int(form.cleaned_data['pincode'])
            phone_number = int(form.cleaned_data['phone_number'])
            reg=models.customer(user=user,customer_name=customer_name, address=address,pincode=pincode,phone_number=phone_number)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully')
        return render(request, 'shop/profile.html')
        


class CustomerRegistartion(View):
    def get(self,request):
        form = CustomerRegistration()
        return render(request,'shop/signup.html',{'form':form})
    def post(self,request):
        form = CustomerRegistration(request.POST)
        if form.is_valid():
            messages.success(request,'congratulations!! registered successfully')
            form.save()
        return render(request,'shop/signup.html',{'form':form}) 



class sellerprofileview(View):
    def get(self,request):
        form=SellerProfileForm()
        return render(request,'shop/sellerprofile.html',{'form':form}) 
    def post(self,request):
        form = SellerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            seller_name = form.cleaned_data[ 'name']
            address = form.cleaned_data['address']
            phone_number = int(form.cleaned_data['phone_num'])
            reg=models.seller(user=user,name=seller_name, address=address,phone_num=phone_number)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully')
            my_group = Group.objects.get(name='vendors') 
            my_group.user_set.add(user)
        return render(request, 'shop/sellerprofile.html', {'form':form})
class productaddview(View):
    def get(self,request):
        form=ProductAddForm()
        return render(request,'shop/addproduct.html',{'form':form}) 
    def post(self,request):
        form = ProductAddForm(request.POST,request.FILES)
        if form.is_valid():
           product = form.save(commit=False)
           vendor= models.seller.objects.get(user=request.user)
           product.seller=vendor
           product.slug=slugify(product.product_title)
           product.save()
           messages.success(request, 'Congratulations!! Product added Successfully')
        return render(request, 'shop/sellerprofile.html', {'form':form})


# def products(request):
#     vendor= models.seller.objects.get(user=request.user)
#     products= models.products.get(seller=vendor)
#     n= len(products)
#     params={'range':range(1,n), 'product': products}
#     return render(request,'shop/products.html',params)