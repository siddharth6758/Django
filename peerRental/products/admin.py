from django.contrib import admin
from products.models import Products

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('prod_id','posted_by','title','rented_by','price','rent_type')