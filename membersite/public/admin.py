from django.contrib import admin

from public.models import Product

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)