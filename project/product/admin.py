from django.contrib import admin

from .models import Brand, Category, Product, ProductLine


class ProductLineInline(admin.TabularInline):
    model = ProductLine
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
