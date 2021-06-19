from shop.forms import Loginform
from django.contrib import admin, auth
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from shop import views
urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('profile/', views.profileview.as_view(), name='profile'),
    path('sellerprofile/', views.sellerprofileview.as_view(), name='sellerprofile'),
    path('addproduct/', views.productaddview.as_view(), name='addproduct'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='shop/login.html', authentication_form=Loginform),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.CustomerRegistartion.as_view(), name='signup'),
    path("products/<int:product_id>/", views.productview, name="productview"),

]
