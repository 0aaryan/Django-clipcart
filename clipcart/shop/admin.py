from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.products)
admin.site.register(models.customer)
admin.site.register(models.cart)
admin.site.register(models.cart_items)
admin.site.register(models.seller)
admin.site.register(models.payment)
