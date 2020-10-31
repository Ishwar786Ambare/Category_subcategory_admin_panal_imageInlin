from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from dummyapp.forms import ProductForm
from dummyapp.models import Product, SubCategory, Category, ProductImage


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductInline(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    model = Product
    form = ProductForm

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js',
        )


# class ProductInline(ImportExportModelAdmin):
#     model = Product
#     form = ProductForm
#
#     class Media:
#         js = (
#             'https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js',
#         )


admin.site.register(Product, ProductInline)
admin.site.register(SubCategory)
admin.site.register(Category)
