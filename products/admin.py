from django.contrib import admin
from .models import Product, Coupon, Cart


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name' , 'price' , 'stock')


class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class CartAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product_name', 'product_amount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Cart, CartAdmin)